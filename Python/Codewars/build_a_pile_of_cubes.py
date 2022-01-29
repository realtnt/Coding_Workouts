'''
    
codewars

6 kyu

Build a pile of Cubes
    
'''


def find_nb(m):
    current_vol = 1
    n = 1
    while True:
        n += 1
        current_vol += n ** 3
        if current_vol == m:
            return n
        elif current_vol > m:
            return -1
