'''
Name: Q5.py
Description: to print  root and pwr of given integer
Author: <priya.a.perumal@accenture.com>
Version: 0.1
Date:04/12/2017
'''
#function to print  root and pwr of given integer
def test_function(num):
    pwr = 2
    root = 1
    ans=''
    while pwr < 6: 
        while root**pwr <= num:
            if root**pwr == num:       
                print("the root is:"+str(root))
                print("the power is:"+str(pwr))
                ans = "True"
            root += 1        
        pwr += 1
        root = 1
    #printing if no such pair of integers exist
    if ans != "True":
        print("No such pair of integers exist")

#getting input from user
num = int(raw_input('Enter a positive integer: ')) 
test_function(num)

