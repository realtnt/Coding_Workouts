'''
    
codewars

7 kyu

List Filtering

'''


def filter_list(l):
    out_list = []
    for element in l:
        if type(element) == int:
            out_list.append(element)
    return out_list
