'''
Name: Q1.py
Description:program to find the GCD of two input number
Author: <priya.a.perumal@accenture.com>
Version: 0.1
Date:04/12/2017
'''


#program to find the GCD of two input number
def computeGCD(num1,num2):
  #choose the smaller number
  if num1 > num2:
    smaller = num2
  else:
    smaller = num1
  for i in range(1, smaller+1):
    if((num1% i == 0) and (num2% i == 0)):
      gcd = i
  return gcd


#getting input from the user
num1 = int(raw_input("enter no1:"))
num2 = int(raw_input("enter no2:"))
gcd=computeGCD(num1,num2)
print("GCD of two input number:"+str(gcd))
