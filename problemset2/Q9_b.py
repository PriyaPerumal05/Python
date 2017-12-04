'''
Name: Q9b).py
Description:program to calculate square root using Newton's Method and square root using Math module and difference between two
estimates
Author: <priya.a.perumal@accenture.com>
Version: 0.1
Date:04/12/2017
'''

#function  to abstract the Newton's Method of calculation Square roots
def NewtonSqrt(a,x):
  y=(x+a/x)/2
  return y
  
def test_square_root(number):
  #fuction call to calculate square root using Newton's Method
  NewtonSqrt1=NewtonSqrt(number,3.0)
  #finding square root using math module
  sqr=math.sqrt(number) 
  #difference square root using Newton's Method and square root using Math module
  difference=NewtonSqrt1-sqr
  print number,NewtonSqrt1,sqr,abs(difference)


#importing math module
import math
#getting input from user
string=raw_input("enter no:")
mylist=[]
mylist=string.split(',')
print(mylist)
print "number      NewtonSqrt       math.sqr           difference"
for i in mylist:
  number=float(i)
  test_square_root(number)
  







