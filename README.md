SublimeLinter-rubocop
=========================

[![Build Status](https://travis-ci.org/SublimeLinter/SublimeLinter-rubocop.svg?branch=master)](https://travis-ci.org/SublimeLinter/SublimeLinter-rubocop)

This linter plugin for [SublimeLinter](http://sublimelinter.readthedocs.org) provides an interface to [rubocop](https://github.com/bbatsov/rubocop). It will be used with files that have the `ruby`, `ruby on rails`, `rspec`, `betterruby` or `ruby experimental` syntaxes.

## Installation
SublimeLinter 3 must be installed in order to use this plugin. If SublimeLinter 3 is not installed, please follow the instructions [here](http://sublimelinter.readthedocs.org/en/latest/installation.html).

### Linter installation
Before using this plugin, you must ensure that `rubocop` is installed on your system. To install `rubocop`, do the following:

1. Install [Ruby](http://ruby-lang.org).

1. Install `rubocop` by typing the following in a terminal:
   ```
   [sudo] gem install rubocop
   ```

1. If you are using `rvm` or `rbenv`, ensure that they are loaded in your shell’s correct startup file. See [here](http://sublimelinter.readthedocs.org/en/latest/troubleshooting.html#shell-startup-files) for more information.

**Note:** This plugin requires `rubocop` 0.15.0 or later.

### Linter configuration
In order for `rubocop` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. Before going any further, please read and follow the steps in [“Finding a linter executable”](http://sublimelinter.readthedocs.org/en/latest/troubleshooting.html#finding-a-linter-executable) through “Validating your PATH” in the documentation.

Once `rubocop` is installed and configured, you can proceed to install the SublimeLinter-rubocop plugin if it is not yet installed.

### Plugin installation
Please use [Package Control](https://sublime.wbond.net/installation) to install the linter plugin. This will ensure that the plugin will be updated when new versions are available. If you want to install from source so you can modify the source code, you probably know what you are doing so we won’t cover that here.

To install via Package Control, do the following:

1. Within Sublime Text, bring up the [Command Palette](http://docs.sublimetext.info/en/sublime-text-3/extensibility/command_palette.html) and type `install`. Among the commands you should see `Package Control: Install Package`. If that command is not highlighted, use the keyboard or mouse to select it. There will be a pause of a few seconds while Package Control fetches the list of available plugins.

1. When the plugin list appears, type `rubocop`. Among the entries you should see `SublimeLinter-rubocop`. If that entry is not highlighted, use the keyboard or mouse to select it.

## Settings
For general information on how SublimeLinter works with settings, please see [Settings](http://sublimelinter.readthedocs.org/en/latest/settings.html). For information on generic linter settings, please see [Linter Settings](http://sublimelinter.readthedocs.org/en/latest/linter_settings.html).

You can configure rubocop exactly the way you would from the command line, using `.rubocop.yml` configuration files. For more information, see the [rubocop documentation](https://github.com/bbatsov/rubocop#configuration).

By default, the linter plugin looks for a config file called `.rubocop.yml` in the current directory and its parents. To override the config file path, you would add this to the linter settings:

```json
"rubocop": {
    "args": ["--config", "path/to/config.yml"]
}
```

## Contributing
If you would like to contribute enhancements or fixes, please do the following:

1. Fork the plugin repository.
1. Hack on a separate topic branch created from the latest `master`.
1. Commit and push the topic branch.
1. Make a pull request.
1. Be patient.  ;-)

Please note that modications should follow these coding guidelines:

- Indent is 4 spaces.
- Code should pass flake8 and pep257 linters.
- Vertical whitespace helps readability, don’t be afraid to use it.
- Please use descriptive variable names, no abbrevations unless they are very well known.

Thank you for helping out!
