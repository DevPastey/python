def selection_sort(arr):


    if len(arr) <= 1:
        return arr

    n = len(arr)
    
    for i in range(n):
        min_index = i
     
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

    
   
    return arr

        
    

print(selection_sort([33, 1, 89, 2, 67, 245]))
print(selection_sort([1, 4, 2, 8, 345, 123, 43, 32, 5643, 63, 123, 43, 2, 55, 1, 234, 92]))