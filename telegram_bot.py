import logging

import requests
from telethon import TelegramClient
from config import Config

logger = logging.getLogger("bot")
logger.setLevel("DEBUG")


class TelegramBotBuilder:
    def __init__(self, token):
        logger.info("Building a new bot.")
        self.bot = TelegramBot(token)

    def with_webhook(self, host):
        self.bot.set_webhook(host)
        return self

    def with_core_api(self, api_id, api_hash):
        client = TelegramClient('anon', api_id, api_hash)
        self.bot.core_api_client = client
        return self

    def get_bot(self):
        return self.bot


class TelegramBot:
    def __init__(self, token):
        self.token = token
        self.bot_api_url = f"{Config.TELEGRAM_API}/bot{self.token}"
        self.core_api_client = None

    def set_webhook(self, host):
        try:
            host = host.replace("http", "https")
            logger.info(f"Setting webhook for url: {host}")
            set_webhook_url = f"{self.bot_api_url}/setWebhook?url={host}"

            response = requests.get(set_webhook_url)
            response.raise_for_status()
            logger.info(f"Got response: {response.json()}")
        except Exception as e:
            logger.error(f"Failed to set webhook: {e}")

    def send_message(self, chat_id, message):
        try:
            logger.info(f"Sending message to chat #{chat_id}")
            send_message_url = f"{self.bot_api_url}/sendMessage"
            response = requests.post(send_message_url, json={"chat_id": chat_id,
                                                              "text": message})
            response.raise_for_status()
        except Exception as e:
            logger.error(f"Failed to send message: {e}")
            raise

    async def get_chat_history(self, chat_id, limit=30):
        try:
            if not self.core_api_client:
                return []
            logger.info(f"Getting conversation history for chat #{chat_id}")
            history = await self.core_api_client.get_messages(chat_id, limit)
            result = [f"{message.sender.first_name} {message.sender.last_name}: {message.message} \n"
                      for message in history if not message.action]
            result.reverse()
            return '\n'.join(result)
        except Exception as e:
            logger.error(f"Failed to get chat history: {e}")
            raise
