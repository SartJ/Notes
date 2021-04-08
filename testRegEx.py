# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 18:59:24 2021

@author: sartaj
"""

import re

'''
Meta Characters (Need to be escaped):-
. ^ $ * + ? { } [ ] \ | ( )
'''

pattern = re.compile(r'[a-c]{3}cab+(da)*f')

matches = pattern.finditer('abcbcaaaabbf')

for match in matches:
    print(match)
    
def matcher(pat):
    pattern = re.compile(r'{}'.format(pat))
    matches = pattern.finditer('abcbcdeade')
    print(pattern)
    for m in matches:
        print(m)
    
    

matcher('a(bc)*de')































































































































