#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Aparajita Fishman
# Contributors: Francis Gulotta, Josh Hagins, Mark Haylock
# Copyright (c) 2013 Aparajita Fishman
#
# License: MIT
#

"""This module exports the Rubocop plugin class."""

from SublimeLinter.lint import RubyLinter


class Rubocop(RubyLinter):
    """Provides an interface to rubocop."""

    syntax = (
        'better rspec',
        'betterruby',
        'cucumber steps',
        'rspec',
        'ruby experimental',
        'ruby on rails',
        'ruby'
    )
    cmd = None
    executable = 'ruby'
    version_args = '-S rubocop --version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 0.34.0'
    regex = (
        r'^.+?:(?P<line>\d+):(?P<col>\d+): '
        r'(:?(?P<warning>[RCW])|(?P<error>[EF])): '
        r'(?P<message>.+)'
    )

    def cmd(self):
        command = ['ruby', '-S', 'rubocop', '--format', 'emacs']

        if self.filename:
            # Ensure the files contents are passed in via STDIN:
            self.tempfile_suffix = None
            command += ['--stdin', path]
        else:
            # File is unsaved, instead set tempfile_suffix so that a tempfile is
            # passed into rubocop, rather than using STDIN (which won't work
            # when we can't provide a hint as to the files whereabouts):
            self.tempfile_suffix = 'rb'

        return command
