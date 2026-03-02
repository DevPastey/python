def dfs(matrix, start_node):
    # This list will be shared by all recursive calls
    visited = []

    def traverse(current_node):
        # 1. Mark the node as visited
        visited.append(current_node)
        
        # 2. Check the row for the current node
        for neighbor, connected in enumerate(matrix[current_node]):
            # 3. If connected and not yet visited, go deeper
            if connected == 1 and neighbor not in visited:
                traverse(neighbor)

    # Start the recursion
    traverse(start_node)
    
    return visited

adj_matrix = [[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0]]
print(dfs(adj_matrix, 1)) 