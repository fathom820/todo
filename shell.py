# These commands are flexible, meaning they can all be used on
# categories, tasks, and steps. 
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
  "help"
]

def listen():
  while True:
    userin = input("todo > ");
    if userin == "exit":
      exit(0)