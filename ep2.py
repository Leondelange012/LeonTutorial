#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Episode 2 - Conditions

#find an input word that meets all conditions! Don't change the code :)
#just read through it and see if you can find a word which passes all tests!
#focus on understanding what the conditions are checking.
"""

word = 'butthole'

if word[2] == 't':
    print('First test passed')
    first = True
else:
    print("FAILED FIRST")



if word[3:5] == 'th':
    print('Second test passed')
    second = True
else:
    print('FAILED SECOND')


if word[-1] != 'e':
    print('FAILED THIRD')
else:
    print('Third test passed')
    third = True



#the len() function gives the length of a variable
if len(word) < 8:
    print('Word is too long! - FAILED Fourth')
elif len(word) > 8:
    print('Word is too short! - FAILED Fourth')
else:
    print('Fourth test passed')
    fourth = True



if word[-8] != 'b':
    print('FAILED Fifth')
else:
    print('Fifth test passed')
    fifth = True



if word[1] != 'u':
    print('FAILED Sixth')
elif word[1] == 'u' and word[-3] == 'o':
    print('Sixth test passed')
    sixth = True
else:
    print('FAILED Sixth')

#don't worry too much about below - this is just to give you an output :)
try:
    if all([first, second, third, fourth, fifth, sixth]):
        print('CONGRATS you ' + word + ' you have passed all tests!')
except Exception as e:
    print('YOU HAVE FAILED ' + word + ' is not the right word')