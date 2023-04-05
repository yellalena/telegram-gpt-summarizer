import asyncio

from quart import Quart, request
import hypercorn.asyncio
from pyngrok import ngrok

from config import Config
from models import Update
from openai_helper import OpenAiHelper
from telegram_bot import TelegramBot

app = Quart(__name__)


@app.route('/', methods=["GET", "POST"])
async def handle_webhook():
    update = Update(**await request.json)
    chat_id = update.message.chat.id

    # process "summarize" command
    if update.message.text.startswith("/summarize"):
        history = await app.bot.get_chat_history(chat_id)
        response = app.openai_helper.get_response("Please, briefly summarize the following conversation history:\n" +\
                                                  history)
    else:
        response = app.openai_helper.get_response(update.message.text)

    app.bot.send_message(chat_id, response)

    return "OK", 200


def run_ngrok(port=8000):
    http_tunnel = ngrok.connect(port)
    return http_tunnel.public_url


@app.before_serving
async def startup():
    host = run_ngrok(Config.PORT)
    app.bot = TelegramBot(Config.TELEGRAM_TOKEN, Config.TELEGRAM_CORE_API_ID, Config.TELEGRAM_CORE_API_HASH)
    app.bot.set_webhook(host)
    app.openai_helper = OpenAiHelper(Config.OPENAI_TOKEN)
    await app.bot.core_api_client.connect()
    await app.bot.core_api_client.start()


async def main():
    quart_cfg = hypercorn.Config()
    quart_cfg.bind = [f"127.0.0.1:{Config.PORT}"]
    await hypercorn.asyncio.serve(app, quart_cfg)


if __name__ == "__main__":
    asyncio.run(main())
