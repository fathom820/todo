# library imports
import os

# local imports
import commands

cmd_list = [
  commands.CommandHelp("help", "Display a list of all commands and their attributes; for more information about 1 command, use \"help [command]\""),
  commands.
]

def listen():
  line = input("todo $ ")
  
  if len(line) > 0:
    line = line.split(" ")
    
  for cmd in cmd_list:
    if line[0] == cmd.keyword:
      cmd.action()
    