# copyfile() = copies contents of a file
# copy()  =  copyfile() + permission mode + destination can be directory
# copy2() =  copy() + copies metadata (file's creation and modification times)

import shutil
# shutil.copyfile('test.txt','copy.txt') #src,dst
shutil.copyfile('test.txt','copy.txt') #src,dst