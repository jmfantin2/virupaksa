import random
import sys
import os

print('\n')

heros = {'Spiderman' : 'Roger Federer', 'Captain America' : 'Steve Rogers', 'Iron Man' : 'Tony Stark'}
your_hero = 'Iron Man'

print('\n' + your_hero + '\'s name is', heros[your_hero])

del heros['Captain America']

heros['Spiderman'] = 'Peter Parker'

print('\n heros LEN:', len(heros))
print('\n heros KEYS:', heros.keys())
print('\n heros VALS:', heros.values())

print('\n get works too:', heros.get('Iron Man'))
print('\n and it\'s great for validation:', heros.get('Captain America'))

print('\n')
