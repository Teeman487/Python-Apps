# slicing = create a substring by extracting elements from another string
#              indexing[] or slice()
#             [start:stop:step]

name = "Bro Code"

first_name = name[:3]
last_name = name[4:8]
funky_name = name[0:8:3]
# funky_name = name[::3]
reversed_name =name[::-1] # edoC orB
print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)

website1 = "http://google.com"
website2 = "http://wikipedia.com"
web = website1[7:-4]
print(web)

slice = slice(7,-4)
print(website1[slice])
print(website2[slice])

