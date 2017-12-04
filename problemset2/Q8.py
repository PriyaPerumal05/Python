'''
Name: Q8.py
Description:program to evaluate the expression using eval() method
Author: <priya.a.perumal@accenture.com>
Version: 0.1
Date:04/12/2017
'''

#function definition for eval() method
def eval_loop(input):
  #eval method to run the python code
  a=eval(input)
  print(a)

#importing built-in math module  
import math 
#getting input from user
input=raw_input("enter:") 
#if the input is done it will exit from the loop
while input!="done":
  #function call
  eval_loop(input)
  input=raw_input("enter")
  