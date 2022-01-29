'''
    
codewars

6 kyu

Is a number prime?

'''

def is_prime(num):
    if num <= 1: return False
    prime = True
    for i in range(2, int(num**0.5)+1):
        if num%i == 0:
            prime = False
    return prime