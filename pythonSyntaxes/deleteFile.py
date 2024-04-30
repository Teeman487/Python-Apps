import os
import shutil

path = "folder"

try:
    # os.remove(path)    # removes only file
    # os.rmdir(path)      # removes only empty folder
    shutil.rmtree(path)  # deletes directory and all files contained in it
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to delete that")
except OSError:
    print("You cannot delete that using that function")
else:
    print(path+" was deleted")
