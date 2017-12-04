'''
Name: Q4b).py
Description:program to calculate total wholesale cost for 60 copies
Author: <priya.a.perumal@accenture.com>
Version: 0.1
Date:04/12/2017
'''

#function to calculate total wholesale cost for 60 copies
def calculatePrice(book):
  discount=book*0.4
  totalprice=(60*discount)+3+(0.75*59)
  return totalprice
  
book=24.95
#function call to calculate total wholesale cost for 60 copies
calculateprice=calculatePrice(book)
print("total wholesale cost for 60 copies:"+str(calculateprice))


