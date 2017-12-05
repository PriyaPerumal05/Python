'''
Name:Q4C).py
Description:program to calculate time at when did i reached for breakfast after running
Author: <priya.a.perumal@accenture.com>
Version: 0.1
Date:05/12/2017
'''


timeleft = 6 * 3600 + 52 *60
easypace = 2 * (8 * 60 + 15 )
fastpace = 3 * (7 * 60 + 12 )
totaltimerun =timeleft+easypace+fastpace
hours = totaltimerun/3600
remainingsec= totaltimerun%3600
minutes = remainingsec/60
seconds = remainingsec% 60
print "reached home for breakfast at:",hours,":",minutes,":",seconds,"AM"
