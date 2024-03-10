from BuckTheDuck.common.generative_ai.base_generative_ai import BaseGenerativeAI
from BuckTheDuck.common.generative_ai.gemini_accessor import GeminiAccessor


class GenerativeAiFactory:

    @classmethod
    def get_accessor(cls, context_message_prefix: str, context_message_suffix: str) -> BaseGenerativeAI:
        return GeminiAccessor(context_message_prefix, context_message_suffix)