# keyword arguments = arguments preceded by an identifier when we pass them to a function
#                       The order of the arguments doesnt matter, unlike positional arguments
#                       Python knows the names of the arguments that our function receives

# Positional Arguments: Order of arguments matter
# def hello(first,middle,last):
#     print("Hello "+first+" "+middle+" "+last)
#
# hello("Bro","Dude","Code")

# Keyword Arguments: Unordered 
def hello(first,middle,last):
    print("Hello "+first+" "+middle+" "+last)

hello(last="Code",middle="Dude",first="Bro")