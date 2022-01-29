def bubbleSort(arr):
    n = len(arr)
    sortPass = 0

    # Traverse through all array elements
    for i in range(n):
        swapped = False

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if swapped == False:
            break
        sortPass += 1
    print("Passes:", sortPass)


# Driver code to test above
numbers = [5, 10, 3, 6, 120, 54, 15, 90, 4,
           8, 3, 84, 55, 42, 435, 55, 77, 46, 7, 1, 4, 3, 6, 4, 7, 6, 8]

bubbleSort(numbers)

print("Sorted array is:")
for i in numbers:
    print(i, end=" ")
