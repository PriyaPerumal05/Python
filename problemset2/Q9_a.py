'''
Name: Q9a).py
Description:program to abstract the Newton's Method of calculation Square roots
Author: <priya.a.perumal@accenture.com>
Version: 0.1
Date:04/12/2017
'''

#function  to abstract the Newton's Method of calculation Square roots
def NewtonSqrt(a,x):
  y=(x+a/x)/2
  print(y)
  
#getting input from user
a=float(raw_input("enter no:"))
x=float(raw_input("enter no:"))
#function call to calculate square root using Newton's Method
NewtonSqrt(a,x)


