# *args =  parameter that will pack all arguments into a tuple
#           useful so that a function can accept a varying amount of arguents

# def add(num1,num2):
#     sum = num1 + num2
#     return sum
#
# print(add(1,2))

def add(*args):
    sum = 0

    args = list(args)  #  cast tuple as a list(changeable)
    args[0] = 0
    for i in args:
        sum +=i # captures all the i's
    return sum

print(add(1,2,3,4,5,6))