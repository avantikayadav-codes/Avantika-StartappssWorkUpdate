class Student:
    def display(self):
        print("Student Details")


class Teacher:
    def display(self):
        print("Teacher Details")


class Employee:
    def display(self):
        print("Employee Details")


def show(obj):
    obj.display()


s = Student()
t = Teacher()
e = Employee()

show(s)
show(t)
show(e)