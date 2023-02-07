#Dictionaries Ordered, no duble, mutable (orberates on key value pars)

student = {1: "john", "age":25, "courses": ["math", "datasci"]}
student["phone"] = "12345678"
student.update({1: "jane", "age": 27, "phone": "87654321", "lastname":"jonson"})
age = student.pop("age")
for key, value in student.items():
    print(key, value)

print(student.keys())
print(student.values())





print(student)
print(age)