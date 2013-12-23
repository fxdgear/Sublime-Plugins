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

_Mac users need to use the function key_: Fn+F7 and Fn+Shift+F7

#### Example

Before:

    import datetime

    class MyClass(object):
        def __init__(self, *args, **kwargs):
            pass

        def my_function(self, *args, **kwargs):
            print date][time.datetime.now()

> ][ denotes cursor location

After pressing f7:

    import ipdb
    import datetime

    class MyClass(object):
        def __init__(self, *args, **kwargs):
            pass

        def my_function(self, *args, **kwargs):
            ipdb.set_trace() ################## Break Point ######################
            print datetime.datetime.now()


> Using shif+f7 will return the code to the "Before" state.

### Key Bindings

In the User Defined keybindings (go to Preferences | User Key Bindings) add the following two keybindings:

	{ "keys": ["f7"], "command": "debug"},
	{ "keys": ["shift+f7"], "command": "undebug"}

### Dependencies

	* Ipython -- `pip install ipython`
	* ipdb -- `pip install ipdb`


## run_external

### Usage

Run External will run the currently selected text (if you have multiple selected regions it only does the first one),
will attempt to run the text as a subprocess and replace the highlighed text with the results.

If you have any suggestions you'd like to see from run_external please feel free to create an issue, and I'll do my
best to see if it's something I can produce!

### Key Bindings

To execute the command you can use the included keymap of "ctrl-r" or you can make your own. _Mac_ users should try "fn-ctrl-r."

    { "keys": ["ctrl+r"], "command": "run_external"}

### Example:

#### Before:

    ]date[

> ][ denotes highlighted text

#### After:

    ]Thu Sep 29 16:27:10 MDT 2011[

> ][ denotes highlighted text

### Simple wget support:

There is very simple wget support at the moment and it's incredibly fragile

Install
-----

Clone this repo into your Sublime Text 2/3 Packages directory. Here are the OS dependent locations (substitute correct version numbers):


* Windows:
    %APPDATA%/Sublime Text 2/Packages/

* OS X:
    ~/Library/Application Support/Sublime Text 2/Packages/

* Linux:
    ~/.Sublime Text 2/Packages/


The package will not work with the key bindings and dependencies that were mentioned above (and are repeated here in the install section for your convenience). Note, _Mac users should insert the key bindings as they appear -- actual usage requires you to prepend with the Function key, but that doesn't need to be included in the key bindings below_.


# Key Bindings

In the User Defined keybindings (go to Preferences | User Key Bindings) add the following two keybindings:

    { "keys": ["f7"], "command": "debug"},
    { "keys": ["shift+f7"], "command": "undebug"}

# Dependencies

    * Ipython -- `pip install ipython`
    * ipdb -- `pip install ipdb`

If you are going to use the "run external" functionality, include this binding as well:

    { "keys": ["ctrl+r"], "command": "run_external"}


