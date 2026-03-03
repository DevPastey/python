def dfs_n_queens(n):

    matrix = [[0]* n   for _ in range(n) ]
    board = [-1] * n
    solution = []
    visited = []
    # print(matrix)
    
    def backtrack(row):
        if n < 1 :
            return []
        if row == n:
            solution.append(board[:])
            return

        
        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1
    
    def is_safe(row, col):
        for prev_row in range(row):
            prev_col = board[prev_row]
            if prev_col == col:
                return False
            if abs(prev_row - row) == abs(prev_col - col):
                return False
        return True
    # return matrix
    # traverse(0)
    backtrack(0)
    return solution
    

print(dfs_n_queens(5))
