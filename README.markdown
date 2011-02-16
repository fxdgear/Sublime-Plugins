Sublime Plugins
=========

* python_debugger

## python_debugger

### Usage

use "F7" / "shift+F7" to insert/remove `ipdb.set_trace()` statements

### Key Bindings

In the User Defined keybindings (goto Preferences | User Key Bindings) add the following two keybindings:

	{ "keys": ["f7"], "command": "debug"},
	{ "keys": ["shift+f7"], "command": "undebug"}

### Dependencies
 
	* Ipython -- `pip install ipython`
	* ipdb -- `pip install ipdb` 


 

Usage
-----
Copy the plugin file (ie. python_debugger.py) and associated keymap file (ie. python_debugger.sublime-keymap) to your Sublime Text "User plugins" directory.
This is located at:

* Windows:
    %APPDATA%/Sublime Text 2/Packages/User/
* OS X:
    ~/Library/Application Support/Sublime Text 2/Packages/User/
* Linux:
    ~/.Sublime Text 2/Packages/User/