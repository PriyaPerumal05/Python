'''
Name: Q5.py
Description: to find sum of the digits in string
Author: <priya.a.perumal@accenture.com>
Version: 0.1
Date:04/12/2017
'''

#to find sum of the digits in string
def sumDigits(s):
  try:
    mylist=[]
    #converting string to a list
    mylist=list(s)
    print mylist
    sum=0
    #for loop to sum the digits
    for i in mylist:
      if i.isdigit()==True:
        sum=sum+int(i)
    return sum
  except Exception as e:
    print(e)


#getting input from user
s=raw_input("enter string:")
sum=sumDigits(s)
#printing sum of the digits in string
print("sum of the digits in string:"+str(sum))
