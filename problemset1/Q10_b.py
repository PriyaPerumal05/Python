'''
Name:Q10b).py
Description:program to print cube root of a positive and negative number
Author: <priya.a.perumal@accenture.com>
Version: 0.1
Date:05/12/2017
'''

x =abs(125)
epsilon = 0.01
numGuesses = 0
low = 0.0
high = max(1.0, x)
ans = (high + low)/2.0
while abs(ans**3 - x) >= epsilon:
   print 'low =', low, 'high =', high, 'ans =', ans
   numGuesses += 1
   if ans**3 < x:
       low=ans
   else:
       high=ans
   ans = (high + low)/2.0
print 'numGuesses =', numGuesses
print ans, 'is close to cube root of', x


x =abs(-125)
epsilon = 0.01
numGuesses = 0
low = 0.0
high = max(1.0, x)
ans = (high + low)/2.0
while abs(ans**3 - x) >= epsilon:
   print 'low =', low, 'high =', high, 'ans =', ans
   numGuesses += 1
   if ans**3 < x:
       low=ans
   else:
       high=ans
   ans = (high + low)/2.0
print 'numGuesses =', numGuesses
print ans, 'is close to cube root of', x



