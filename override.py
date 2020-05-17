#!/usr/bin/env python

class Person(object):
    def __init__(self):
        print("Calling Person Constructor1111!!!")
   
    def __init__(self,name):
        print("Calling Person Constructor!!!")
        self.name = name

    def getDetails(self):
        print("Calling Person Details Method!!!")
        return self.name

class Student(Person):
    def __init__(self,name,branch,year):
        print("Calling student constructor")
        self.branch = branch
        self.year = year

    def getDetails(self):
        print("Calling student details method!!!")
        return "%s studies %s and in %s year."%(self.name,self.branch,self.year)

class Teacher(Person):
    def __init__(self,name):
        print("Calling teacher constructor")
        Person.__init__(self,name)

    def getDetails(self):
        print("Calling teacher details method!!!")

person1 = Person("Bruno")
print(person1.getDetails())
student1 = Student("Anil","CS",2008)
print(student1.getDetails())
teacher1 = Teacher("Sarfaraaz")
print(teacher1.getDetails())
