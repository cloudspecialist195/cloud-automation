import os

def show_tree(folder, indent=""):
    item_list = sorted([e for e in os.listdir(folder) if not e.startswith(".")]) # a list of all items inside the variable (folder)
    for item in item_list: # list all items vertically with "indent + ├── " infront of each item
        print(indent + "├── " + item) 
       
       # os.path.isdir() - Is it TRUE that this path is a folder?
       # before using os.path.isdir(), must use os.path.join() to show full path of the variable and its items 
        full_path = os.path.join(folder, item) # a full path is needed in order to use os.path.isdir()
        if os.path.isdir(full_path): # This function to trace subfolders (and if it is TRUE), 
            show_tree(full_path, indent + "│   ") # Then, call func def show_tree() for the subfolders and add this "│   "
   
    

show_tree(".") # call at current folder

