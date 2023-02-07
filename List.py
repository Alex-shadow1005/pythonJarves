##LIST Ordered, allow duble, mutable

a = [1,3,5,7,9,11]

c = []
for x in a:
    c.append(x*2)
print(c)

d = [x * 2 for x in a]
print(d)

courses = ["math", "his", "dataSci"]
courses_2 = ["finanse", "IT-sec"]
courses.append("cooking")
print(courses[2])
print(courses[-1])
print(courses[:3])
courses.insert(3, "art")
courses.extend(courses_2)
print(courses)