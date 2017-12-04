'''
Name: Q3.py
Description: print the largest odd number among them
Author: <priya.a.perumal@accenture.com>
Version: 0.1
Date:04/12/2017
'''
#test function to print the largest odd number among them
def test_function(mylist):
  #defining empty list
  mylist1=[]
  
  #split the string using split function adding it to the list
  mylist1=mylist.split(',')
 
  #printing the values in the list
  print(mylist1)
  
  #defining empty list
  mylist2=[]

  #for loop to find odd nos in a list
  for i in mylist1:
    if(int(i)%2!=0):
      mylist2.append(int(i))
  #printing odd nos:
  print("odd nos are:"+str(mylist2))
  
  #printing all the nos are even if the nos are even 
  if(len(mylist2)==0):
    print("all nos are even")
    
  #printing largest odd no if the nos are odd:
  else:
    print("largest odd no is:"+str(max(mylist2)))  

#getting input from user
mylist=raw_input("enter 10 numbers :")

#function call
test_function(mylist)
    