#!/usr/bin/python

class Marks:
    def __init__(self,marks,subject):
        self.marks=marks
        self.subject=subject
        print("Inside constructor __init__")
        print("self.marks = ",self.marks," self.subject = ",self.subject)

    def __str__(self):
        print("Inside constructor (__str__)")
        return 'Total marks %d obtained in %s'%(self.marks,self.subject)

    def __add__(self,other):
        print("Inside constructor (__add__)")
        return Marks(self.marks+other.marks,self.subject+','+other.subject)

m1 = Marks(80,"Math")
m2 = Marks(90,"Science")
m3 = Marks(70,"English")
m4 = Marks(60,"Hindi")
m5 = Marks(50,"K2J2")

print(m1+m2+m3+m4+m5)



