def find_anagram_words(list_1, list_2):
    
   
    sorted_tuple1 = {tuple(sorted(word)) for word in list_1}
    sorted_tuple2 = {tuple(sorted(word)) for word in list_2}
    
    common_tuples = sorted_tuple1 & sorted_tuple2
    
    list1_output = [word for word in list_1 if tuple(sorted(word)) in common_tuples]
    list2_output = [word for word in list_2 if tuple(sorted(word)) in common_tuples]
    
    output = []
    
    
    for word1 in list1_output:
        for word2 in list2_output:
            if ( tuple(sorted(word1)) == tuple(sorted(word2)) ) and (word1 != word2):
                output.append((word1))

    
    
    
    return (output)
    
    
    
    
        

print(find_anagram_words(['cinema', 'iceman'], ['iceman', 'cinema'])) # should return ['cinema', 'iceman']
print(find_anagram_words(['test', 'stet'], ['tent', 'nett'])) # should return []
print(find_anagram_words(['hello', 'world'], ['dolly', 'sir'])) # should return []