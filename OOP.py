class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self):
        return '{} - {} -{}'.format(self.name,self.age, self.grade)


    def get_grade(self):
        return self.grade



class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
        self.athleats = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def add_athleat(self, athleat):
        if len(self.athleats) < self.max_students:
            self.athleats.append(athleat)
            return True
        return False

    def get_average_grade(self):
        value=0
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)

    def get_avarage_run_speed(self):
        value = 0
        for athleat in self.athleats:
            value += athleat.get_run_speed()
        return value / len(self.athleats)

class Athleat(Student):
    def __init__(self, name, age, grade, run_speed):
        super().__init__(name, age, grade)
        self.run_speed = run_speed

    def __str__(self):
        return '{} - {} -{} -{}'.format(
            self.run_speed)



    def get_run_speed(self):
        return self.run_speed

s1 = Athleat("alex", 18, 7, 19)
s2 = Student("jakob", 12, 10)
s3 = Athleat("anders", 22, 12, 20.1)

course = Course("it-Sec", 3)
course2 = Course("Gym", 2)
course.add_student(s1)
course.add_student(s2)
course.add_student(s3)
course2.add_athleat(s1)
course2.add_athleat(s3)
print(course.get_average_grade())
print(course2.get_avarage_run_speed())
print(s1)
print(s2)

