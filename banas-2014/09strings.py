import random
import sys
import os

print('\n')

long_string = 'i\'ll catch you if you fall - The Floor'
print(long_string.capitalize())
print('index of "fall":', long_string.find('fall'))
print('[0:4]',long_string[0:4])
print('[-5:]',long_string[-5:])
print('[:-5]',long_string[:-5])
print('[:4]',long_string[:4] + ' kick a hole in the wall.')
print('isalpha()',long_string.isalpha())
print('isalnum()',long_string.isalnum())
print('strip()',long_string.strip())

long_string.replace('Floor', 'Ground')

words = long_string.split(' ')

print('\n')
print(words)

char = 'N'
adjective = 'favorite'
print('\n%c is my %s letter and my score is %.2f' % (char, adjective, 2.2222))

print('\n')
