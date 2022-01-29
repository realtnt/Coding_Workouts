'''
    
codewars

7 kyu

Printer Errors

'''

import re


def printer_error(s):
    return f"{len(re.findall('[n-z]', s))}/{len(s)}"
