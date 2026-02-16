def quick_sort(input):
    if len(input) == 0:
        return input
    
    pivot = input[0]

    

    

    less = [x for x in input if x < pivot]
    equal = [x for x in input if x == pivot]
    greater = [x for x in input if x > pivot]

    return quick_sort(less) + equal + quick_sort(greater)

print(quick_sort([20, 3, 14, 1, 5]))