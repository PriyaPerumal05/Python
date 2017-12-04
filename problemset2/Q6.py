'''
Name: Q6.py
Description: to find the first even number in list of integers
Author: <priya.a.perumal@accenture.com>
Version: 0.1
Date:04/12/2017
'''

#function to find the first even number in list of integers
def findAnEven(l):
  try:
    mylist=[]
    mylist=l.split(',')
    for i in mylist:
      if int(i)%2==0:
        return int(i)
        break
      
  except ValueError as e:
    print("No even numbers in list!")
  
    
#getting from the user
l=raw_input("enter an list:")
even=findAnEven(l)
if(even==None):
  print "no even nos in the list"
else:
  print("first even no in the list:"+str(even))
