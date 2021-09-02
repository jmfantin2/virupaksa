import random
import sys
import os

grocery_list = ['Juice', 'Tomatoes', 'Carrots']
print('\nFirst of grocery list:', grocery_list[0])

grocery_list[0]='Soda'
grocery_list.append('Rice')
grocery_list.insert(1, 'Onions')
grocery_list.remove('Soda')
print('\n First two of grocery list: ', grocery_list[0:2])

grocery_list.sort()
grocery_list.reverse()

other_events = ['Wash car', 'Pick up kids']

to_do_list = [other_events, grocery_list]
print('\nTo do list', to_do_list)

print('\nItem [1] of grocery_list from to_do_list:', to_do_list[1][1])

merged_list = other_events + grocery_list
print('Merged list LEN:', len(merged_list))
print('Merged list MIN:', min(merged_list))
print('Merged list MAX:', max(merged_list))
