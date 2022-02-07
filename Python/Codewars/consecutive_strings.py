'''
    
codewars

6 kyu

Consecutive strings
    
'''


def longest_consec(strarr, k):
    if strarr == []:
        return ''
    if k > len(strarr) or k <= 0:
        return ''

    max_length = 0
    max_string = ''
    for index in range(len(strarr)-k+1):
        if len(''.join(strarr[index:index+k])) > max_length:
            max_string = ''.join(strarr[index:index+k])
            max_length = len(''.join(strarr[index:index+k]))
    return max_string


print(longest_consec(["zone", "abigail", "theta",
      "form", "libe", "zas"], 2), "abigailtheta")
print(longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb",
      "oocccffuucccjjjkkkjyyyeehh"], 1), "oocccffuucccjjjkkkjyyyeehh")
print(longest_consec([], 3), "")
print(longest_consec(["itvayloxrp", "wkppqsztdkmvcuwvereiupccauycnjutlv", "vweqilsfytihvrzlaodfixoyxvyuyvgpck"],
      2), "wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfixoyxvyuyvgpck")
print(longest_consec(["wlwsasphmxx", "owiaxujylentrklctozmymu",
      "wpgozvxxiu"], 2), "wlwsasphmxxowiaxujylentrklctozmymu")
print(longest_consec(
    ["zone", "abigail", "theta", "form", "libe", "zas"], -2), "")
print(longest_consec(["it", "wkppv", "ixoyx", "3452",
      "zzzzzzzzzzzz"], 3), "ixoyx3452zzzzzzzzzzzz")
print(longest_consec(["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], 15), "")
