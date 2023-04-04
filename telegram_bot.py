import requests

from config import Config


class TelegramBot:
    def __init__(self, token):
        self.token = token
        self.bot_api_url = f"{Config.TELEGRAM_API}/bot{self.token}"

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

