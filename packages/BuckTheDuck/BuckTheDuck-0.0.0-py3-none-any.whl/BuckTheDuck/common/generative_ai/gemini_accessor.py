import os
import google.generativeai as genai

from BuckTheDuck.common.generative_ai.base_generative_ai import BaseGenerativeAI
from common.generative_ai.config import Config


class GeminiAccessor(BaseGenerativeAI):

    def _create_client(self):
        config = Config()
        GOOGLE_API_KEY = config.generative_ai_token
        genai.configure(api_key=GOOGLE_API_KEY)
        return genai.GenerativeModel('gemini-pro')

    def _send_message(self, message: str) -> str:
        response = self._client.generate_content(message)
        return response
