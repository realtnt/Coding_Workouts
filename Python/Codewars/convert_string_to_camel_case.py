'''
    
codewars

6 kyu

Convert string to camel case
    
'''
import re


def to_camel_case(text):
    if text == '':
        return ''
    out = [word.title() for word in re.split('[_-]', text)]
    print(out)
    print(text)
    if text[0] >= 'a' and text[0] <= 'z':
        out[0] = out[0].lower()
    return ''.join(out)
