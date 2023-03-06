#!/usr/bin/env python
# coding: utf-8

# In[1]:


#TASK6


# In[3]:


def is_valid(board, row, col):
    
    # check the column
    for i in range(row):
        if board[i] == col:
            return False
    # check the diagonal
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i] == j:
            return False
    for i, j in zip(range(row-1, -1, -1), range(col+1, len(board))):
        if board[i] == j:
            return False
    return True

def n_queens_helper(n, row, board, solutions):
    
    if row == n:
        # we found a valid solution
        solutions.append(board[:])
        return
    for col in range(n):
        if is_valid(board, row, col):
            board[row] = col
            n_queens_helper(n, row+1, board, solutions)

def n_queens(n):
    
    board = [-1] * n
    solutions = []
    n_queens_helper(n, 0, board, solutions)
    return solutions

def dfs_n_queens(n):
    solutions = []
    def dfs_helper(queens, xy_dif, xy_sum):
        y = len(queens)
        if y == n:
            solutions.append(queens)
            return
        for x in range(n):
            if x not in queens and (y-x) not in xy_dif and (y+x) not in xy_sum:
                dfs_helper(queens+[x], xy_dif+[y-x], xy_sum+[y+x])
    dfs_helper([],[],[])
    return solutions

def bfs(n):
    queue = [[(i, 0)] for i in range(n)]
    while queue:
        path = queue.pop(0)
        if len(path) == n:
            return path
        col = len(path)
        for row in range(n):
            if all(path[i][1] != row and abs(path[i][1] - row) != col - i for i in range(col)):
                queue.append(path + [(col, row)])
    return None


# In[ ]:




