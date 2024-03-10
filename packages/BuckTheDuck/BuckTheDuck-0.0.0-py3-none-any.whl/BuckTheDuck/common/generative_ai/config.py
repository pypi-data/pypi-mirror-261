from common.singleton import Singleton


class Config(Singleton):
    _generative_ai_type = ''
    _generative_ai_token = ''

    @property
    def generative_ai_type(self):
        return self._generative_ai_type

    @generative_ai_type.setter
    def generative_ai_type(self, generative_ai_type: str):
        self._generative_ai_type = generative_ai_type

    @property
    def generative_ai_token(self):
        return self._generative_ai_token

    @generative_ai_token.setter
    def generative_ai_token(self, generative_ai_token: str):
        self._generative_ai_token = generative_ai_token
