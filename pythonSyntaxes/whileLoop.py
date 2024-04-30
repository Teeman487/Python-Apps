# while loop = a statement that will execute it's block of code
#                    as long as it's condition remains true
#
# while 1==1:
#       print("Help! I'm stuck in a loop!")

# name = ""
name = None  # can only concatenate str (not "NoneType") to str

# while len(name) == 0:
while not name: # indicates None
       name= input("Enter your name: ")# We are stuck until we enter something
print("Hello "+str(name))