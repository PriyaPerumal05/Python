'''
Name: Q4.py
Description: to find the decimal equivalent of the binary number 10011 
Author: <priya.a.perumal@accenture.com>
Version: 0.1
Date:04/12/2017
'''


#calculating decimal equivalent of the binary number 10011
def test_function(binary):
  pwr=0
  decimal=0
  while binary!=0:
    temp=binary%10
    decimal=decimal+temp*2**pwr
    binary=binary/10 
    pwr+=1
  print("decimal equivalent of the binary number 10011 is:"+str(decimal))


binary=10011
#passing binary value to the function:(fuction call)
test_function(binary)