#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Aparajita Fishman
# Copyright (c) 2013 Aparajita Fishman
#
# License: MIT
#

"""This module exports the Rubocop plugin class."""

import os
from SublimeLinter.lint import RubyLinter, util


class Rubocop(RubyLinter):

    """Provides an interface to rubocop."""

    syntax = 'ruby'
    executable = 'rubocop@ruby'
    regex = r'^.+?:(?P<line>\d+):(?P<col>\d+): .+?: (?P<message>.+)'
    tempfile_suffix = 'rb'

    def cmd(self):
        """
        Return the command line to be run.

        We define this to find a .rubocop.yml file.

        """

        command = self.executable_path + ['--format', 'emacs']
        config = util.find_file(os.path.dirname(self.filename), '.rubocop.yml')

        if config:
            command += ['--config', config]

        return command
