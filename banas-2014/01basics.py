import random
import sys
import os

print('\nWhat is your name?')
name = sys.stdin.readline()
print('\nHello', name, '\n')

print('5 +2 =', 5+2)
print('5 -2 =', 5-2)
print('5 *2 =', 5*2)
print('5 /2 =', 5/2)
print('5 %2 =', 5%2)
print('5**2 =', 5**2)
print('5//2 =', 5//2, '\n')

quote = '\"it\'s not a good day if you didn\'t start it winning\"'
multi_line_quote = '''We knew the world would not be the same.
Few people laughed. Few people cried. Most people were silent.'''

print('%s %s' % (multi_line_quote, '\n— Robert Oppenheimer\n'))

# Comment

'''
Multiline comment
'''
