# library imports
import sys


class Command:
  
  # keyword: called to invoke command
  # desc: description of command shown in the
  #   help menu
  def __init__(self, keyword, desc):
    self.keyword = keyword
    self.desc = desc
    
  # to be overwritten by every child class
  def action():
    pass

  
class CommandHelp(Command):
  def __init__(self, keyword, desc):
    Command.__init__(self, keyword, desc)

  def action(self):
    print("Help")
    #TODO
    
class CommandToday(Command):
  def __init__(self, keyword, desc):
    Command.__init__(self, keyword, desc)
    
  def action(self):
    print("Today: ")
    #TODO

class CommandExit(Command):
  def __init__(self, keyword, desc):
    Command.__init__(self, keyword, desc)
    
  def action(self):
   print("exit")
   sys.exit() 

cmd_list_static = [
  CommandHelp("help", "Display a list of all commands and their attributes; for more information about 1 command, use \"help [command]\""),
  CommandToday("today", "Display today's agenda and tasks to complete."),
  CommandExit("quit", "Exit the Toad shell.")
]

cmd_list_flex = [

]