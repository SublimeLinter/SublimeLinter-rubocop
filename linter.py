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
    cmd = 'bundle exec rubocop --format emacs'
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 0.15.0'
    regex = (
        r'^.+?:(?P<line>\d+):(?P<col>\d+): '
        r'(:?(?P<warning>[RCW])|(?P<error>[EF])): '
        r'(?P<message>.+)'
    )
    tempfile_suffix = 'rb'
    config_file = ('--config', '.rubocop.yml')
