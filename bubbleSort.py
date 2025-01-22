def bubble_sort(arr):
    n = len(arr)  # Get the length of the list
    for i in range(n):
        # Flag to check if any swapping occurred in this pass
        swapped = False
        # Last i elements are already in place, no need to compare them
        for j in range(0, n-i-1):
            # If the current element is greater than the next, swap them
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Swap
                swapped = True
        
        # If no swapping happened in the inner loop, the list is already sorted
        if not swapped:
            break


my_list = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(my_list)
print("Sorted list:", my_list)
