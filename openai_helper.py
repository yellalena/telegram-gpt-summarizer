import logging

import openai

logger = logging.getLogger("bot")
logger.setLevel("DEBUG")


class OpenAiHelper:
    def __init__(self, token, model="gpt-3.5-turbo"):
        logging.info(f"Initializing OpenAI helper. Selected model: {model}")
        openai.api_key = token
        self.model = model

    def get_response(self, message_text):
        try:
            logging.info(f"Getting response from OpenAI. Message: {message_text}")
            response = openai.ChatCompletion.create(model=self.model,
                                                    messages=[{"role": "user", "content": message_text}])
            return response.choices[0].message.content
        except Exception as e:
            logging.error(f"Failed to get response from OpenAI: {e}")
            raise
