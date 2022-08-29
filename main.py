#!/usr/bin/python3

# Author: Michael Frank

# library imports
import os

# local imports
import filesys
import shell


if __name__ == "__main__":
  # setup
  if not os.path.exists(filesys.home):
    os.mkdir(filesys.home)
  
  # important!
  os.chdir(filesys.home)
  
  if len(os.listdir()) == 0:
    print("Performing first-time setup...")
    filesys.initialize()
    print("Created category Tasks.")
    
  
  shell.listen()
    
  