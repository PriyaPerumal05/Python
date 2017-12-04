'''
Name: Q3.py
Description: to find the factorial of a number using iterative and recursive implementation
Author: <priya.a.perumal@accenture.com>
Version: 0.1
Date:04/12/2017
'''

#fuction to find the factorial of a number using iterative implementation
def factI(n):
  fact=1
  i=1
  while n>0:
    fact=fact*i
    i=i+1
    n=n-1
  return fact
  
#fuction to find the factorial of a number using recursive implementation
def factR(n):
  if  n==0:
    return 1
  else:
    number=n*factR(n-1)
    return number

#getting no from the user  
n=raw_input("enter no:")
#fuction call for iterative implementation
factorial=factI(int(n))
print("factorial of a number using iterative implementation:"+str(factorial))
#fuction call for recursive implementation
fact=factR(int(n))
print("factorial of a number using recursive implementation:"+str(fact))
