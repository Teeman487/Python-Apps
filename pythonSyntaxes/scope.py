# scope = The regio that a variable is recognized
#         A variable is only available from inside the region it is created.
#         A global and locally scoped versions of a variable can be created.

name = "Bro"  # global scope (available inside & outside functions)

def display_name():
    name = "Code"  # local scope  (available only inside this function)
    print(name)   # Enclose

display_name()
print(name)

# L = Local
# E = Enclosing
# G = Global
# B = Built-in

