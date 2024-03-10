from unidiff import PatchSet, PatchedFile

from BuckTheDuck import get_logger
from generative_ai.generator_interface import GeneratorInterface

logger = get_logger()


class CommitGenerator(GeneratorInterface):
    _LOG_PREFIX = 'CommitGenerator'
    _COMMIT_ROLES = {
        'SINGLE_COMMENT': {
            'PREFIX': 'You are a skilled developer and you are about '
                      'to create a commit message for the following changes:',
            'SUFFIX': 'Please create meaningful commit message that summarize the changes and provide the overall effect of the changes'
        },
        'SUMMARIZE': {
            'PREFIX': 'You are a skilled developer and review your commit changes and want to make them shorter focus on the overall changes ',
            'SUFFIX': ''
        }
    }

    def generate_commit_message(self, git_difference: PatchSet) -> str:
        diff_changes = ''
        file: PatchedFile
        commit_message = ''
        for file in git_difference:
            if len(diff_changes) > 1000:
                commit_message_genai_response = self._generative_ai_accessor_for_commenting.send_message(diff_changes)
                commit_message += commit_message_genai_response.text + '\n'
                diff_changes = ''
            else:
                if file.is_added_file:
                    diff_changes += (f'new file: {file.path}\n' + str(file))
                elif file.is_modified_file:
                    diff_changes += (f'modified file: {file.path}\n' + str(file))
                elif file.is_removed_file:
                    diff_changes += f'removed file: {file.path}'
                diff_changes += '\n\n'

        if len(diff_changes) > 0:
            commit_message_genai_response = self._generative_ai_accessor_for_commenting.send_message(diff_changes)
            commit_message += commit_message_genai_response.text

        logger.info(f'{self._LOG_PREFIX}: {commit_message=}')
        if len(commit_message.split('\n')) > self._MAX_NUMBER_OF_ROWS_FOR_COMMIT:
            finalized_commit_message = self._generative_ai_accessor_for_auditing.send_message(commit_message)
            commit_message = finalized_commit_message.text

        return commit_message
