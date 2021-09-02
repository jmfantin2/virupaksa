import random
import sys
import os

print('\n')

age = 30

permission = ''
if age >= 21 : permission = 'you can drive cars and tractor trailers'
elif age >= 16 : permission = 'you can only drive cars'
else : permission = 'you can\'t drive at all'

print('\n', permission)

if ((age >= 1) and (age <= 18)): 
  print('\nyou get a birthday party :)')
elif (age == 21) or (age >= 65):
  print('\nyou get a rubber duck :)')
elif not(age == 30) or (age >= 65):
  print('\nyou get to sweep the house :(')
else: print('you get a nice mug of water. we keep the mug tho.')


print('\n')
