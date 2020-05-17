#!/usr/bin/python

print("\n Example Program - 1: Class & Instance\n")
class Student:
    'Common base class for all student'
    studentCount = 0
    def __init__(self,name,fee,age):
        self.name = name
        self.fee = fee
        self.age = age
        Student.studentCount += 1

    def displayCount(self):
        print("Total Students %d"%Student.studentCount)

    def displayStudent(self):
        print("Nme  : ", self.name, ", Fee: ", self.fee)

    def displayAge(self):
        print("Nme  : ", self.name, ", Fee: ", self.fee)

    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name,"destroyed")

student1 = Student("Ebby", 2500,17)
student1.displayStudent()
student1.displayAge()

print("\nExample Program - 2 Accessing attributes\n")
print("hasattr: ", hasattr(student1,'age'))
print("getattr: ", getattr(student1,'age'))
print("setattr: ", setattr(student1,'age',20))
print("getattr called after setattr: ", getattr(student1,'age'))
print("delattr: ", delattr(student1,'age'))
print("hasattr: ", hasattr(student1,'age'))

print("\nExample 3: Built in class attributes\n")
print("Student.__doc__:",Student.__doc__)
print("Student.__name__:",Student.__name__)
print("Student.__module__:",Student.__module__)
print("Student.__bases__:",Student.__bases__)
print("Student.__dict__:",Student.__dict__)

print("Total students %d" %Student.studentCount)

print("\nExample Program -- 4: Destroying objects (Garbage collector)\n")
print("Object id: ",id(student1))

del student1
