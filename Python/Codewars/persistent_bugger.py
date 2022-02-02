'''
    
codewars

6 kyu

Persistent Bugger

'''


def persistence(n):
    def convert_to_list(number): return [int(x) for x in str(number)]
    number_list = convert_to_list(n)
    if len(number_list) < 2:
        return 0

    times = 0
    while len(number_list) >= 2:
        product = 1
        for i in range(len(number_list)):
            product *= number_list[i]
        number_list = convert_to_list(product)
        times += 1
    return times
