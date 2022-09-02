# library imports
import os

# local imports
import commands

flex_commands = [
  "add",
  "edit",
  "info",
  "remove",
  "done"
]

# will accept arguments but can't be used to modify anything
static_commands = [
  "today",
  "tomorrow",
  "calendar",
  "help",
  "quit"
]


def listen():
  line = input("todo $ ")
  
  if len(line) > 0:
    line = line.split(" ")
    
  # static command checking
  for cmd in commands.cmd_list_static:
    if len(line) != 1:
      print("Error: command does not accept arguments.")
      return

    if line[0] == cmd.keyword:
      cmd.action()    