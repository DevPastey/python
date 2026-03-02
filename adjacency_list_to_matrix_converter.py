
def adjacency_list_to_matrix(param):
    num_of_node = len(param.keys())
    # print(num_of_node)
    ans = [[0] * num_of_node for _ in range(num_of_node)]


    for node, neighbours in param.items():   
        for neighbour in neighbours:
            ans[node][neighbour] = 1
      
    for i in range(num_of_node):
        print(ans[i])
    
    return ans

print(adjacency_list_to_matrix({0: [1], 1: [0]}))

print(adjacency_list_to_matrix({0: [2], 1: [2, 3], 2: [0, 1, 3], 3: [1, 2]}))



