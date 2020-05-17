#!/usr/bin/python

# Lambda function example
print("\nExample Program 1 - Anonymous Function Lambda\n")
total = lambda s1,s2,s3,s4,s5:s1+s2+s3+s4+s5

#Now call total as a function
print("Student1 total marks : ",total(90,70,85,80,67))
print("Student2 total marks : ",total(10,30,45,50,78))

def func_ref(list):
    print("List values before append are : ",list)
    list.append([90,75,68,54])
    print("List values after append are : ",list)
    return

list = [60,70,80]
print("Example Program 2: Passby assignment\n")
print("List values before function call are : ",list)
func_ref(list)
print("List values after function call are : ",list)

# Pass by value
def func_value(obj):
    # To change passed parameter into function
    obj = 90
    print("Values inside the function: ", obj)
    return

obj = 80

print("Example Program 3: Passby value\n")
print("obj values before function call are : ",obj)
func_value(obj)
print("obj values after function call are : ",obj)

#Global and local variables

print("Example Program 4 - Global Values\n")

sum = 500

def total(s1,s2,s3,s4,s5):
    sum = s1+s2+s3+s4+s5
    print("Inside the function :",sum)
    return sum

total(90,85,95,85,70)
print("Outside the function : ",sum)
