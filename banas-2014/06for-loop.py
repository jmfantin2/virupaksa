import random
import sys
import os

print('\n')

for n in range( 0, 10 ):
  print(n, ' ', end='')

print('\n')

for n in [3,5,8,13,21,34]:
  print(n*1.618, ' ', end='')

print('\n')

band_list = ['Tool', 'Deftones', 'Incubus']

for b in band_list: print(b)

print('\n')

num_list = [[1,2,3],[10,20,30],[100,200,330]]

for x in range(0,3):
  for y in range(0,3):
    print(num_list[x][y])

print('\n')
