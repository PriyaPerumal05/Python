'''
Name: Q8.py
Description: to print the ratios of two list
Author: <priya.a.perumal@accenture.com>
Version: 0.1
Date:04/12/2017
'''

#to print the ratios of two list
def getRatios(vect1,vect2):
  #try block to print the ratios of two list
  try:
    print(vect1)
    print(vect2)
    length=len(vect1)
    length1=len(vect2)
    vect3=[]
    i=0
    
    if(length==length1):
      while(i<length):
        a=int(vect1[i])/int(vect2[i])
        vect3.insert(i,a)
        i+=1
      return vect3
      
    #print if the length is not equal of two list
    else:
      print("length is not equal of two list")
  
  #except block if it is not a list
  except Exception as e:
    print(e)
    
#getting input from user
a=raw_input("enter list")
b=raw_input("enter list")
vect1=[]
vect2=[]
vect1=a.split(',')
vect2=b.split(',')
vect4=[]
#function call 
vect4=getRatios(vect1,vect2)
print("ratios of two list:")
print(vect4)

