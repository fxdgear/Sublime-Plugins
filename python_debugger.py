import sublime, sublimeplugin
import subprocess

BREAK_POINT = "ipdb.set_trace()  ################## Break Point ######################"

class DebugCommand(sublime_plugin.TextCommand):
    """Command to automatically import ipdb and set_trace at the current line"""
    def run(self, edit):
        print edit.__dict__
        # current position to place break point
        current_pos = self.view.sel()[0]
        current_line = self.view.line(current_pos)
        current_string = self.view.substr(current_line)
        tab_count = len(current_string) - len(current_string.lstrip())
        
        hard_tabs=False
        if current_string[0] == "\t":
            hard_tabs=True

        if hard_tabs:
            tabs = "\t"*tab_count
        else:
            tabs = " "*tab_count
        
        self.view.insert(edit, current_line.begin(), u'%s%s\n' % (tabs, BREAK_POINT)) 
        
        first_line = self.view.line(self.view.text_point(0,0))
        line_contents = self.view.substr(first_line)
        # Check if import ipdb is already the first line
        if line_contents != "import ipdb":
            # python debugger is not imported yet so make line1 of file the debugger import statement
            self.view.insert(edit, first_line.begin(), u'import ipdb\n') 
        


class UndebugCommand(sublime_plugin.TextCommand):
    """
    Command to undo debugging statements.

    Note: This is ugly right now.
    When iterating through a the list of view.split_by_newlines if a debug statement gets deleted.
    It screws up up the the line count somewhere and the program exits quitely.

    What I'm doing here is re-creating the list of lines after the removal of each debug statement
    removal.

    """
    def run(self, edit):
        debug_line = self.find_debug_line(sublime.Region(0, self.view.size()))
        while debug_line:
            self.view.erase(edit, debug_line)
            debug_line=self.find_debug_line(sublime.Region(0, self.view.size()))

    
    def find_debug_line(self, region_set):
        for line in self.view.split_by_newlines(region_set):
            if self.view.substr(line).strip() in ["import ipdb", BREAK_POINT]:
                return self.view.full_line(line)
        return None
        

class RunExternalCommand(sublimeplugin.TextCommand):
    """
    Runs an external command with the selected text,
    which will then be replaced by the command output.
    """
    
    def run(self, view, args):
        if view.sel()[0].empty():
            # nothing selected: process the entire file
            region = sublime.Region(0L, view.size())
        else:
            # process only selected region
            region = view.line(view.sel()[0])

        p = subprocess.Popen(
            args,
            shell   = True,
            bufsize = -1,
            stdout  = subprocess.PIPE,
            stderr  = subprocess.PIPE,
            stdin   = subprocess.PIPE)

        output, error = p.communicate(view.substr(region).encode('utf-8'))

        if error:
            sublime.errorMessage(error.decode('utf-8'))
        else:
            view.replace(region, output.decode('utf-8'))
