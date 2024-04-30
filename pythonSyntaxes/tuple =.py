# tuple =  collection which is ordered and unchangeable
#            used to group together related data

student = ("Bro",21,"male")
print(student.count(student[0]))
print(student.index("male"))

for x in student:
    print(x)

if "Bro" in student:
    print("Bro is here")