'''
    
codewars

6 kyu

Sort the odd
    
'''


def sort_array(source_array):
    odds_positions = []
    odds = []
    sorted_array = source_array
    for i, element in enumerate(source_array):
        if element % 2 != 0:
            odds_positions.append(i)
            odds.append(element)
    sorted_odds = sorted(odds)
    for i, pos in enumerate(odds_positions):
        sorted_array[pos] = sorted_odds[i]
    return sorted_array
