from timeit import timeit
from random import randint


def merge(list_a, list_b):
    list_sorted = []
    while list_a != [] and list_b != []:
        if list_a[0] > list_b[0]:
            list_sorted.append(list_b.pop(0))
        else:
            list_sorted.append(list_a.pop(0))
    if list_a == []:
        list_sorted.extend(list_b)
    else:
        list_sorted.extend(list_a)
    return list_sorted


def merge_sort(unsorted):
    if len(unsorted) <= 1:
        return unsorted
    list_a = unsorted[:len(unsorted)//2]
    list_b = unsorted[len(unsorted)//2:]
    return merge(merge_sort(list_a), merge_sort(list_b))


def bubble_sort(unsorted):
    sorted = unsorted[:]
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(sorted)-1):
            if sorted[i] > sorted[i+1]:
                sorted[i], sorted[i+1] = sorted[i+1], sorted[i]
                swapped = True
    return sorted


def bubble_sort_opt(unsorted):
    sorted = unsorted[:]
    list_length = len(unsorted)-1
    swapped = True
    while swapped:
        swapped = False
        for i in range(list_length):
            if sorted[i] > sorted[i+1]:
                sorted[i], sorted[i+1] = sorted[i+1], sorted[i]
                swapped = True
        list_length -= 1
    return sorted


def bs(): return bubble_sort(list_to_sort)


def bso(): return bubble_sort_opt(list_to_sort)


def ms(): return merge_sort(list_to_sort)


def ps(): return sorted(list_to_sort)


while True:
    for i in range(100):
        print("\n")

    no_of_elements = int(input("How big do you want the list to be? "))

    # Generate a large (1000 items) random list
    random_list = [randint(0, 100000) for i in range(no_of_elements)]
    sorted_list = list(range(no_of_elements))
    reverse_sorted_list = list(range(no_of_elements, 1, -1))
    nearly_sorted = sorted_list.copy()
    nearly_sorted[0] = no_of_elements

    type_of_list = input(
        "Select type of list:\n1. Random\n2. Sorted\n3. Reverse order\n4. Nearly sorted\nYour selection: ")
    # Create anonymous functions to use with timeit, be sure to check these function names match your pasted ones

    if type_of_list == "1":
        list_to_sort = random_list
    elif type_of_list == "2":
        list_to_sort = sorted_list
    elif type_of_list == "3":
        list_to_sort = reverse_sorted_list
    else:
        list_to_sort = nearly_sorted

    print(f"Timsort (Python built-in sort) took: {timeit(ps, number=100):.5f}")
    # time the functions for 100 runs each
    print(f"Merge took: {timeit(ms, number=100):.5f}")
    #print(timeit(ms, number=100))

    print(f"Bubble took: {timeit(bs, number=100):.5f}")

    print(f"Bubble optimised took: {timeit(bso, number=100):.5f}")

    exit_program = input("\n\nDo you want to have another go? ")
    if exit_program.lower() != "y":
        exit()
