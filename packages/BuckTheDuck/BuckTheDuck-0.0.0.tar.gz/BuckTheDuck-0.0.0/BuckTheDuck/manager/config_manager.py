import json
import os
from enum import Enum
from getpass import getpass
from pathlib import Path

from common.exceptions import UnsupportedOperation
from common.generative_ai.config import Config


class SupportedGenAI(Enum):
    GEMINI = 'gemini'

    @classmethod
    def to_list(cls):
        return [
            cls.GEMINI.value
        ]


class ConfigKeys(Enum):
    GENAI_TYPE = 'genai_type'
    GENAI_TOKEN = 'genai_token'


class ConfigManager:
    _CONFIG_DIR = f'{Path.home()}/.BuckTheDuck'

    def init(self):
        if not os.path.exists(self._CONFIG_DIR):
            self._init_config_file()

        self._add_project()

    def load_config(self):
        config = self._load_config_file()
        config_instance = Config()
        if config[ConfigKeys.GENAI_TYPE.value] and config[ConfigKeys.GENAI_TOKEN.value]:
            config_instance.generative_ai_type = config[ConfigKeys.GENAI_TYPE.value]
            config_instance.generative_ai_token = config[ConfigKeys.GENAI_TOKEN.value]
        else:
            print(f'We are missing an parameter to start working, please run again the \'init\' command')
            raise UnsupportedOperation()

    def _load_config_file(self):
        try:
            with open(f'{self._CONFIG_DIR}/config', 'r') as config_file:
                config = json.load(config_file)
        except FileNotFoundError:
            config = {
                ConfigKeys.GENAI_TYPE.value: '',
                ConfigKeys.GENAI_TOKEN.value: ''
            }
        return config

    def _init_config_file(self):
        os.mkdir(self._CONFIG_DIR)
        config = {
            ConfigKeys.GENAI_TYPE: 'gemini',
            ConfigKeys.GENAI_TOKEN: ''
        }
        self._write_content_to_config_file(config)

    def _add_project(self):
        config = self._load_config_file()

        genai_type_input = input(f'Enter Gen AI type: {SupportedGenAI.to_list()} ')
        if genai_type_input not in SupportedGenAI.to_list():
            print(f'{genai_type_input} is not a supported Gen AI type, but soon it will!')
            raise UnsupportedOperation()
        genai_token = getpass('Enter Gen AI Token: ')
        config[ConfigKeys.GENAI_TYPE.value] = genai_type_input
        config[ConfigKeys.GENAI_TOKEN.value] = genai_token

        self._write_content_to_config_file(config)

    def _write_content_to_config_file(self, config):
        with open(f'{self._CONFIG_DIR}/config', 'w') as config_file:
            config_file.write(json.dumps(config))
