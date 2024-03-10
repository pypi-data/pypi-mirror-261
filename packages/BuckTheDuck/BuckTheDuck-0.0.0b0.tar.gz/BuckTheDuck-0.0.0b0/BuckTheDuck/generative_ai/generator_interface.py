from abc import ABC

from BuckTheDuck.common.generative_ai.generative_ai_factory import GenerativeAiFactory


class GeneratorInterface(ABC):
    _LOG_PREFIX = 'GeneratorInterface'
    _MAX_NUMBER_OF_ROWS_FOR_COMMIT = 10
    _COMMIT_ROLES = {
        'SINGLE_COMMENT': {
            'PREFIX': '',
            'SUFFIX': ''
        },
        'SUMMARIZE': {
            'PREFIX': '',
            'SUFFIX': ''
        }
    }

    def __init__(self):
        self._generative_ai_accessor_for_commenting = (
            GenerativeAiFactory.get_accessor(self._COMMIT_ROLES['SINGLE_COMMENT']['PREFIX'],
                                             self._COMMIT_ROLES['SINGLE_COMMENT']['SUFFIX']))
        self._generative_ai_accessor_for_auditing = (
            GenerativeAiFactory.get_accessor(self._COMMIT_ROLES['SUMMARIZE']['PREFIX'],
                                             self._COMMIT_ROLES['SUMMARIZE']['SUFFIX']))

