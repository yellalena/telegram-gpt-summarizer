from flask import Flask, request
from pyngrok import ngrok

from config import Config
from models import Update
from openai_helper import OpenAiHelper
from telegram_bot import TelegramBot

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def handle_webhook():
    update = Update(**request.json)
    chat_id = update.message.chat.id

    response = app.openai_helper.get_response(update.message.text)
    app.bot.send_message(chat_id, response)

    return "OK", 200


def run_ngrok(port=8000):
    http_tunnel = ngrok.connect(port)
    return http_tunnel.public_url


def main():
    app.bot = TelegramBot(Config.TELEGRAM_TOKEN)
    host = run_ngrok(Config.PORT)
    app.bot.set_webhook(host)
    app.openai_helper = OpenAiHelper(Config.OPENAI_TOKEN)
    app.run(port=Config.PORT, debug=True, use_reloader=False)


if __name__ == "__main__":
    main()