'''
Name: Q10a).py
Description:program to replace x=25 by x=-25
Author: <priya.a.perumal@accenture.com>
Version: 0.1
Date:04/12/2017
'''


x =abs(-25)
epsilon = 0.01
numGuesses = 0
low = 0.0
high = max(1.0, x)
ans = (high + low)/2.0
while abs(ans**2 - x) >= epsilon:
   print 'low =', low, 'high =', high, 'ans =', ans
   numGuesses += 1
   if ans**2 < x:
       low=ans
   else:
       high=ans
   ans = (high + low)/2.0
print 'numGuesses =', numGuesses
print ans, 'is close to square root of', x




output:
code runs infinitely
