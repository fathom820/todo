
# API for converting data into files and directories in ~/.todo

import os

home = os.path.expanduser("~") + "/.todo/"

def initialize():
  os.chdir(home)
  os.mkdir("Tasks")
  
def add_cat(cat):
  os.chdir(home)

  if os.path.exists(cat):
    print("Category already sxists.")
    return

  os.mkdir(cat)
    
def add_task(cat, task):
  os.chdir(home)
  
  if os.path.exists(cat + "/" + task):
    print("Task already exists in this category.")
    return
  
  os.m
  