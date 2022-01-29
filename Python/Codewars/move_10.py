'''
    
codewars

7 kyu

Move 10

'''


def move_ten(st):
    return ''.join([chr((ord(letter)+10-ord('a')) % 26+ord('a')) for letter in st])
