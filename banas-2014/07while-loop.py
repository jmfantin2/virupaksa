import random
import sys
import os

print('\n')

random_num = random.randrange(0,100)

while(random_num != 15):
  print(random_num)
  random_num = random.randrange(0,100)

print('\n')

i = 0

while (i<=20):
  if(i%2==0):
    print(i)
  elif(i==9):
    break

  i += 1

print('\n')
