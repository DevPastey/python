def repeating_elements(nums):
    
    seen = set()
    dupl = set()
    
    for num in nums:
        if num in seen:
            dupl.add(num)
        else:
            seen.add(num)
    
    return list(dupl)
        
    # if the num exist update it's 'count +=1
    # return num with count greater than 1     

print(repeating_elements([9, 8, 7, 8, 7, 6, 5]))  # expected output : [8, 7]
# print(repeating_elements([-1, 2, 3, -1, 2, 3]))   # expected output : [-1, 2, 3]
# print(repeating_elements([1, 2, 3, 4, 5]))        # expected output : []







def exclusive_products(inventory1, inventory2):
    arr1 = [x.upper() for x in inventory1]
    arr2 = [x.upper() for x in inventory2]
    
    ex1 = set(arr1)
    ex2 = set(arr2)
    
    A = sorted(list(ex1 - ex2))
    B = sorted(list(ex2 - ex1))
    
    return A, B
    
inventory1 = ["Shirt", "Jeans", "Hat"]
inventory2 = ["jeans", "Belt", "Boots"]
print(exclusive_products(inventory1, inventory2))
# Expected output: (['HAT', 'SHIRT'], ['BELT', 'BOOTS'])

inventory1 = ["T-Shirt", "hoodie", "Backpack"]
inventory2 = ["Backpack", "Hoodie", "t-shirt"]
print(exclusive_products(inventory1, inventory2))
# Expected output: ([], [])

inventory1 = []
inventory2 = ["Dress", "Skirt", "Coat"]
print(exclusive_products(inventory1, inventory2))
# Expected output: ([], ['COAT', 'DRESS', 'SKIRT'])