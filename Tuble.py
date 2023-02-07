##Tuble ordered ,allow duble, immutable

#Comprehension

a =[1,3,5,7,9,11]

d = (i for i in a)
print(tuple(d))
print(d)

courses = ("math", "his", "datasci", "math")
for i in courses:
    print(i)
print(courses.count("math"))
print(courses.index("his"))
courses.append("art")
