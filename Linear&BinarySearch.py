# Linear Search :
def linear_search(arr, target):
    for i in range(len(arr)): 
        if arr[i] == target:  
            return i  
    return -1  


my_list = [10, 20, 30, 40, 50]
target_value = 30

result = linear_search(my_list, target_value)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not foundn")



# Binary Search :-  


def binary_search(arr, target):
    low = 0  
    high = len(arr) - 1 
    
    while low <= high:
        mid = (low + high) // 2  
        
        if arr[mid] == target:  
            return mid  
        elif arr[mid] < target: 
            low = mid + 1 
        else:  
            high = mid - 1  
    
    return -1 


my_list = [10, 20, 30, 40, 50]  
target_value = 30

result = binary_search(my_list, target_value)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")

   