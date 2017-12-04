'''
Name: Q2.py
Description:program to find a is the power of b
Author: <priya.a.perumal@accenture.com>
Version: 0.1
Date:04/12/2017
'''


#function to find a is the power of b
def is_power(a,b):
  c=a/b
  if a%b==0 and c%b==0 :
    return "True"
  else:
    return "False"
  
#getting input from user
a=int(raw_input("enter power:"))
b=int(raw_input("enter base:"))
c=''
c=is_power(a,b)
if c=='True':
  print('a is the power of b')
else:
  print("a is not the power of b")

