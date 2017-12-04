'''
Name: Q7.py
Description: program to  check whether it is a palindrome or not
Author: <priya.a.perumal@accenture.com>
Version: 0.1
Date:04/12/2017
'''

#test function to check whether it is a palindrome or not
def testIsPalindrome(string):
  a=isPalindrome(string)
  if a=="True":
    print "it is a palindrome"
  else:
    print "it is not a palindrome"

#palindrome fuction to check whether it is a palindrome or not and either it  return true or return false 
def isPalindrome(s):
  length=len(s)
  print("length of the string:"+str(length))
  i=0
  while(length>0):
    if s[i]==s[length-1]:
      i=i+1
      length=length-1
    else:
      return "False"
  return "True"

#getting input from the user
string=raw_input("enter a string:")
#function call to check whether it is a palindrome or not
testIsPalindrome(string)

