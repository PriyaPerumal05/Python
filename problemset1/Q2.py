'''
Name: Q2.py
Description: print the right justify string
Author: <priya.a.perumal@accenture.com>
Version: 0.1
Date:04/12/2017
'''
#function to print the right justify string
def right_justify(s):
  #calculating length of the string
  a=len(s)
  #calulating spaces required before the string
  spacerequired=70-a
  spaces=' ' * spacerequired 
  #appending string and spaces
  string=spaces + s
  #printing right justify string
  print(string)
  
#getting string from user
s=raw_input("enter string")
#passing string using function
right_justify(s)
