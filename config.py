import os


class Config:
    TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    PORT = os.getenv("TELEGRAM_BOT_PORT", 5000)
    TELEGRAM_API = "https://api.telegram.org"
    OPENAI_TOKEN = os.getenv("OPENAI_TOKEN")

