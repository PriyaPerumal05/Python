'''
Name: Q7.py
Description: to check if either string occurs anywhere in the other
Author: <priya.a.perumal@accenture.com>
Version: 0.1
Date:04/12/2017
'''

#function to check if either string occurs anywhere in the other
def isIn(x,y):
   index=x.find(y)
   index1=y.find(x)
   if index==-1 or index1==-1:
    return "False"
   else:
    return "True"
   

#getting string from user
a=raw_input("enter string1")
b=raw_input("enter string2")
c=isIn(a,b)
if c=="True":
  print "True"
else:
  print "False"


