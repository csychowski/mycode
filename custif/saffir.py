#!/usr/bin/env python3

""" Sample pyhton program to ask for wind speed and produce output"""

windspeed = int(input("What is the wind speed in mph? "))

# Check what Category
if windspeed >= 157:
   message = 'Category 5 - Say a prayer'
elif windspeed >= 130:
   message = 'Category 4 - Catastrophic damage will occur'
elif windspeed >= 111:
   message = 'Category 3 - Devastating damage will occur'
elif windspeed >= 96:
   message = 'Category 2 - Extremely dangerous winds will cause extensive damage'
elif windspeed >= 74:
   message = 'Category 1 - Very dangerous winds will produce some damage'
else:
   message = 'Go out for a walk its nice outside'
print(message)
