import requests
from telethon import TelegramClient
from config import Config


class TelegramBot:
    def __init__(self, token, api_id, api_hash):
        self.token = token
        self.bot_api_url = f"{Config.TELEGRAM_API}/bot{self.token}"
        self.core_api_client = TelegramClient('anon', api_id, api_hash)

    def set_webhook(self, host):
        host = host.replace("http", "https")
        set_webhook_url = f"{self.bot_api_url}/setWebhook?url={host}"
        response = requests.get(set_webhook_url)
        response.raise_for_status()

    def send_message(self, chat_id, message):
        send_message_url = f"{self.bot_api_url}/sendMessage"
        response = requests.post(send_message_url, json={"chat_id": chat_id,
                                                          "text": message})
        response.raise_for_status()

    async def get_chat_history(self, chat_id, limit=30):
        if not self.core_api_client:
            return []
        history = await self.core_api_client.get_messages(chat_id, limit)
        result = [f"{message.sender.first_name} {message.sender.last_name}: {message.message} \n"
                  for message in history if not message.action]
        result.reverse()
        return '\n'.join(result)
