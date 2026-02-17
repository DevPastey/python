def verify_card_number(digits):
    pin = digits.replace(" ", "").replace("-", "")
    arr = [int(x) for x in pin]
    arr.reverse()
    
    result = []
    # final_arr = arr.pop()
    
    print(arr)
    
    for i, digit in enumerate(arr):
        print (i, digit)
        if i == 0:
            continue
        if i % 2 != 0:  
           doubled =  digit * 2
           arr[i] = doubled
        else:
            result.append(digit)
    arr.reverse() 
    print(arr)


print(verify_card_number('453914881'))
