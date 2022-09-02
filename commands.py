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
    
    