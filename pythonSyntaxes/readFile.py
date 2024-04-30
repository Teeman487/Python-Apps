
# try:
#     with open('test.txt') as file:
#        print(file.read())
# except FileNotFoundError:
#     print("That file was not found")
# print(file.closed)

# text = "Heyyy\nThis is some text\nHave a good one!\n"
#
# with open('test.txt','w') as file:
#     file.write(text)

text = "Have a nice day! See ya"

with open('test.txt','a') as file:
    file.write(text)