'''
Name: Q6.py
Description: print the sum of the numbers in s
Author: <priya.a.perumal@accenture.com>
Version: 0.1
Date:04/12/2017
'''
# print the sum of the numbers in s
def test_function(s):
  mylist=[]
  #split the string using split function and adding it to the list 
  mylist=s.split(',')
  #print the string in the list
  print(mylist)
  sum=0
  #for loop to sum the numbers
  for i in mylist:
    sum=sum+float(i)
  #printing sum of the numbers
  print("sum of the numbers:"+str(sum))

#getting input from user
s=raw_input("enter the string in decimal nos")
test_function(s)
