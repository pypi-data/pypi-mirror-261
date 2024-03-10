import os
from enum import Enum
from pathlib import Path
from typing import List

from BuckTheDuck.common.git_providers.git_accessor import GitAccessor
from BuckTheDuck.generative_ai.commit_generator import CommitGenerator
from BuckTheDuck.manager.config_manager import ConfigManager
from BuckTheDuck.common.exceptions import UnsupportedOperation
from BuckTheDuck.generative_ai.code_reviewer_generator import CodeReviewerGenerator
from BuckTheDuck.generative_ai.ticket_progress_generator import TicketProgressGenerator


class CliManager:
    HOME = '~'

    def __init__(self):
        self._config_manager = ConfigManager()

    def run(self, command: str, argv: List[str]):
        if command not in AvailableCommands.to_list():
            command = AvailableCommands.HELP.value
        if command == AvailableCommands.INIT.value:
            self._init_env()
        if command == AvailableCommands.HELP.value:
            self._print_help_menu()
        self._config_manager.load_config()
        if command == AvailableCommands.COMMIT.value:
            self._commit_changes()
        if command == AvailableCommands.COMMIT_AND_PUSH.value:
            self._commit_and_push()
        if command == AvailableCommands.BRANCH_SUMMARIZE.value:
            self._summarize_branch_changes(argv)
        if command == AvailableCommands.CODE_REVIEW.value:
            self._run_code_review()

    def _print_help_menu(self):
        print('Available Commands: ')
        print('1. init - Initiate Buck to work with your favorite GenAI provider  ')
        print('2. commit - Generate commit message per your changes and commit it  ')
        print('3. cop - Generate commit message per your changes and commit & push it  ')
        print('4. branch_summarize - Generate message for your changes in a '
              'branch before merging back to source branch  ')
        print('5. code review - Generate a code review feedback ')
        print('6. help - List available commands')

    def _normalize_path(self, path):
        if '~' in path:
            path = path.replace(self.HOME, str(Path.home()))
        return path

    def _commit_changes(self):
        current_working_directory = os.getcwd()
        git_accessor = GitAccessor(current_working_directory, current_working_directory)
        patch_set = git_accessor.get_last_commit_differences()
        commit_generator = CommitGenerator()
        commit_message = commit_generator.generate_commit_message(patch_set)
        git_accessor.commit(commit_message)

    def _commit_and_push(self):
        self._commit_changes()
        current_working_directory = os.getcwd()
        git_accessor = GitAccessor(current_working_directory, current_working_directory)
        git_accessor.push()

    def _init_env(self):
        config_manager = ConfigManager()
        config_manager.init()

    def _summarize_branch_changes(self, argv):
        try:
            branch_name = argv[0]
            source_branch_name = argv[1]
        except:
            raise UnsupportedOperation('This command require argument for branch name')
        current_working_directory = os.getcwd()
        git_accessor = GitAccessor(current_working_directory, current_working_directory)
        gitlog = git_accessor.get_branch_changes(branch_name, source_branch_name)
        ticket_progress_generator = TicketProgressGenerator()
        message = ticket_progress_generator.generate_message(gitlog)
        # TODO: need to add connector to project management (JIRA and friends)

    def _run_code_review(self):
        current_working_directory = os.getcwd()
        git_accessor = GitAccessor(current_working_directory, current_working_directory)
        patch_set = git_accessor.get_last_commit_differences()
        code_review_generator = CodeReviewerGenerator()
        code_review_generator.generate_message(patch_set)


class AvailableCommands(Enum):
    HELP = 'help'
    INIT = 'init'
    COMMIT = 'commit'
    PUSH = 'push'
    COMMIT_AND_PUSH = 'cop'
    BRANCH_SUMMARIZE = 'branch_summarize'
    CODE_REVIEW = 'cr'

    @classmethod
    def to_list(cls):
        return [cls.HELP.value,
                cls.COMMIT.value,
                cls.COMMIT_AND_PUSH.value,
                cls.INIT.value,
                cls.BRANCH_SUMMARIZE.value,
                cls.CODE_REVIEW.value]