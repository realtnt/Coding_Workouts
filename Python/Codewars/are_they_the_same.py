'''
    
codewars

6 kyu

Are they the "same"?

'''


def comp(array1, array2):
    if array1 == None or array2 == None:
        return False
    array1_sqr = [el**2 for el in array1]
    return sorted(array1_sqr) == sorted(array2)
