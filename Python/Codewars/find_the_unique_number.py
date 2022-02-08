'''
    
codewars

6 kyu

Find the unique number
    
'''


def find_uniq(arr):
    a, b = set(arr)
    return b if arr[0:3].count(a) > 1 else a


print(find_uniq([1, 1, 1, 2, 1, 1]))
print(find_uniq([0, 0, 0.55, 0, 0]))
