import openai


class OpenAiHelper:
    def __init__(self, token, model="gpt-3.5-turbo"):
        openai.api_key = token
        self.model = model

    def get_response(self, message_text):
        response = openai.ChatCompletion.create(model=self.model,
                                                messages=[{"role": "user", "content": message_text}])
        return response.choices[0].message.content
