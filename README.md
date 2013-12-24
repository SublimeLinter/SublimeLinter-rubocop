SublimeLinter-rubocop
=========================

This linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter3) provides an interface to [rubocop](https://github.com/bbatsov/rubocop). It will be used with files that have the “Ruby” syntax.

## Installation
SublimeLinter 3 must be installed in order to use this plugin. If SublimeLinter 3 is not installed, please follow the instructions [here](https://github.com/SublimeLinter/SublimeLinter.github.io/wiki/Installation).

### Linter installation
Before using this plugin, you must ensure that `rubocop` is installed on your system. To install `rubocop`, do the following:

1. Install [Ruby](http://ruby-lang.org).

1. Install `rubocop` by typing the following in a terminal:
   ```
   [sudo] gem install rubocop
   ```

1. If you are using `rvm` or `rbenv`, ensure that they are loaded in your shell’s correct startup file. See [here](https://github.com/SublimeLinter/SublimeLinter.github.io/wiki/Usage#shell-startup-files) for more information.

Once rubocop is installed, you can proceed to install the SublimeLinter-rubocop plugin if it is not yet installed.

### Plugin installation
Please use [Package Control](https://sublime.wbond.net/installation) to install the linter plugin. This will ensure that the plugin will be updated when new versions are available. If you want to install from source so you can modify the source code, you probably know what you are doing so we won’t cover that here.

To install via Package Control, do the following:

1. Within Sublime Text, bring up the [Command Palette](http://docs.sublimetext.info/en/sublime-text-3/extensibility/command_palette.html) and type `install`. Among the commands you should see `Package Control: Install Package`. If that command is not highlighted, use the keyboard or mouse to select it. There will be a pause of a few seconds while Package Control fetches the list of available plugins.

1. When the plugin list appears, type `rubocop`. Among the entries you should see `SublimeLinter-rubocop`. If that entry is not highlighted, use the keyboard or mouse to select it.

## Settings
For general information on how SublimeLinter works with settings, please see [Settings](https://github.com/SublimeLinter/SublimeLinter.github.io/wiki/Settings). For information on generic linter settings, please see [Linter Settings](https://github.com/SublimeLinter/SublimeLinter.github.io/wiki/Linter-Settings).

You can configure rubocop exactly the way you would from the command line, using `.rubocop.yml` configuration files. For more information, see the [rubocop documentation](https://github.com/bbatsov/rubocop#configuration).

**Note:** This plugin finds the nearest `.rubocop.yml` file and uses the `--config` command line argument to use that file, so you may not use the `--config` argument in the linter settings.

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
