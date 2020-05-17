#!/usr/bin/python

class Student:
    studentCount = 0
    def __init__(self,name,age,fee):
            self.name = name
            self.age = age
            self.fee = fee
            Student.studentCount += 1

    def displayDetails(self):
        print("The name of the student is %s and the age of the student is %d and the fee taken is %f "%(self.name,self.age,self.fee))

    def __del__(self):
        class_name = self.__class__.__name__
        print("Class ", class_name," destroyed")

s1 = Student("Saurabh",32,21000)
s1.displayDetails()
print("hasattr:",hasattr(s1,"age"))
print("getattr:",getattr(s1,"age"))
del s1

    
