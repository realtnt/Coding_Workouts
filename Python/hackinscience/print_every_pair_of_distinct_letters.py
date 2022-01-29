'''
    
hackinscience.org

Basics #18

Provide a script printing every possible pairs of two different letters.
    
'''

from string import ascii_lowercase
for i in ascii_lowercase:
    for j in ascii_lowercase:
        if i != j:
            print(i, j, sep='')
