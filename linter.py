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

from SublimeLinter.lint import Linter


class Rubocop(Linter):

    """Provides an interface to rubocop."""

    syntax = ('ruby', 'ruby on rails', 'rspec')
    cmd = 'rubocop --format emacs'
    regex = r'^.+?:(?P<line>\d+):(?P<col>\d+): .+?: (?P<message>.+)'
    tempfile_suffix = 'rb'
    config_file = ('--config', '.rubocop.yml')
