'''
Name: Q1.py
Description: print the largest odd number among them
Author: <priya.a.perumal@accenture.com>
Version: 0.1
Date:04/12/2017
'''

#test function to print largest odd number among them 
def test_function(x,y,z):
  mylist=[]
  if(x%2!=0):
    mylist.append(x)
  if(y%2!=0):
    mylist.append(y)
  if(z%2!=0):
    mylist.append(z)
  max=0
  #printing odd nos
  print("odd numbers are:"+str(mylist))
  #for loop to check largest odd nos
  for i in mylist:
    if(max<i):
      max=i
  #printing which is the largest odd no
  if(max==x):
    print("x is largest odd number")
  elif(max==y):
    print("y is largest odd number")
  elif(max==z):
    print("z is largest odd number")
  else:
    print("all the numbers are even")
    
#getting the input from user
x=int(raw_input("enter no x"))
y=int(raw_input("enter no y"))
z=int(raw_input("enter no z"))
test_function(x,y,z)


