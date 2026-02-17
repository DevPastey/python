def verify_card_number(digits):
    pin = digits.replace(" ", "").replace("-", "")
    arr = [int(x) for x in pin]
    arr.reverse()
    
    result = []

    string = []
    
    # print(arr)
    
    for i, digit in enumerate(arr):
        if i == 0:
            continue
        if i % 2 != 0:  
            doubled =  digit * 2
            arr[i] = doubled
            if doubled > 9:
                doubled -= 9
                arr[i] = doubled
        else:
            result.append(digit)
    arr.reverse() 
    sum_total = sum(arr)
    if sum_total % 10 == 0:
        return "VALID!"
    else:
        return "INVALID!"



print(verify_card_number('453914881'))

print(verify_card_number('453914889'))

print(verify_card_number('4111-1111-1111-1111'))

print(verify_card_number('453914881'))
