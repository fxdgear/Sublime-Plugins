Sublime Plugins
=========

* python_debugger
* run_external

## python_debugger

### Usage

Use "F7" / "shift+F7" to insert/remove `ipdb.set_trace()` statements on current line.
Takes into consideration indentation and tab preference.
Enter as many `ipdb.set_trace()` commands as you like. Only one import statement is ever used.
"shift+f7" will remove _all_ debug statements.

**Mac users** need to use the function key: Fn+F7 and Fn+Shift+F7 (see note at the end of Install section).

#### Example

Before:

    import datetime

    class MyClass(object):
        def __init__(self, *args, **kwargs):
            pass

        def my_function(self, *args, **kwargs):
            print date][time.datetime.now()

> ][ denotes cursor location

After pressing F7:

    import ipdb
    import datetime

    class MyClass(object):
        def __init__(self, *args, **kwargs):
            pass

        def my_function(self, *args, **kwargs):
            ipdb.set_trace() ################## Break Point ######################
            print datetime.datetime.now()


> Using Shift+F7 will return the code to the "Before" state.

### Key Bindings

In the User Defined keybindings (go to Preferences | User Key Bindings) add the following two key bindings:

    { "keys": ["F7"], "command": "debug"},
    { "keys": ["Shift+F7"], "command": "undebug"}

### Dependencies

    * Ipython -- `pip install ipython`
    * ipdb -- `pip install ipdb`


Install
-----

Clone this repo into your Sublime Text 2/3 Packages directory. Here are the OS dependent locations (substitute correct version numbers):


* Windows:
    %APPDATA%/Sublime Text 2/Packages/

* OS X:
    ~/Library/Application Support/Sublime Text 2/Packages/

* Linux:
    ~/.Sublime Text 2/Packages/


The package will not work with the key bindings and dependencies that were mentioned above (and are repeated here in the install section for your convenience). **Mac users** should insert the key bindings as they appear -- actual usage requires you to prepend with the Function key, but the Function key should not be included in the key bindings below.


### Key Bindings

In the User Defined keybindings (go to Preferences | User Key Bindings) add the following two keybindings:

    { "keys": ["F7"], "command": "debug"},
    { "keys": ["Shift+F7"], "command": "undebug"}

### Dependencies

    * Ipython -- `pip install ipython`
    * ipdb -- `pip install ipdb`


###Note to Mac users###

By default, Apple has already assigned some of your function keys. The plugin will work fine with the instructions above, but if you would like to have full control of your keyboard's function keys you can learn how to do that [here](https://support.apple.com/kb/HT3399). The would allow you to insert the debug command with a simple F7 rather an Fn-F7 and to remove the debug commands with Shift-F7 rather than Fn-Shift-F7.