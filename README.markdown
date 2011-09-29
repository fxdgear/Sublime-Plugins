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

In the User Defined keybindings (goto Preferences | User Key Bindings) add the following two keybindings:

	{ "keys": ["f7"], "command": "debug"},
	{ "keys": ["shift+f7"], "command": "undebug"}

### Dependencies
 
	* Ipython -- `pip install ipython`
	* ipdb -- `pip install ipdb` 


## run_external

### Usage

Run External will run the currently selected text (if you have multiple selected regions it only does the first one),
will attempt to run the text as a subprocess and replace the highlighed text with the results.

### Key Bindings

To execute the command you can use the included keymap of "ctrl-r" or you can make your own.

    { "keys": ["ctrl+r"], "command": "run_external"}
    
### Example:

#### Before:

    ]date[
    
> ][ denotes highlighted text
    
#### After:

    ]Thu Sep 29 16:27:10 MDT 2011[

> ][ denotes highlighted text

Install
-----
Checkout this repo into your sublime text 2 Packages directory.
This is located at:

* Windows:
    %APPDATA%/Sublime Text 2/Packages/
* OS X:
    ~/Library/Application Support/Sublime Text 2/Packages/
* Linux:
    ~/.Sublime Text 2/Packages/