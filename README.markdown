Sublime Plugins
=========

* python_debugger

## python_debugger

use "F7"/"shift+F7" to insert/remove `ipdb.set_trace()` statements

* ipdb is required. 
   * `pip install ipython`
   * `pip install ipdb` 
* NOTE: copy the contets of 'python_debugger.sublime-keymap' to the User defined keymap settings (Preferences | User Key Bindings). I'm not sure what the problem is right now but when tying to use plugin defined keymaps, they don't get loaded right.

 

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