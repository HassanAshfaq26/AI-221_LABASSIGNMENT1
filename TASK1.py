#!/usr/bin/env python
# coding: utf-8

# In[1]:


graph={
    'g':['c','i'],
    'c':['b','e'],
    'i':['h','j'],
    'b':['a'],
    'e':['d','f'],
    'h':[ ],
    'j':['k'],
    'a':[ ],
    'd':[ ],
    'f':[ ],
    'k':[ ]
}


# In[2]:


visited=set()
def dfs(visited,graph,node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited,graph,neighbour)
            


# In[3]:


dfs(visited,graph,'g')


# In[ ]:


# CODE IMPLEMENTATION OF BFS IN GRAPHS


# In[14]:


import collections


# In[4]:


graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A'],
    'C': ['A', 'D'],
    'D': ['A', 'C', 'E'],
    'E': ['D'],
}


# In[15]:


def bfs(g,root):

    
    queue = collections.dequeue([root])
    visited=[]

    while queue:
        node=queue.popleft()
        if node not in visited:
            visited.append(node)
        for item in g[node]:
            if item not in visited:
                 queue.append(item)
    print(visited)
             
               


# In[ ]:





# In[19]:


graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A'],
    'C': ['A', 'D'],
    'D': ['A', 'C', 'E'],
    'E': ['D'],
}

def bfs(node):

    visited = [False] * (len(graph))

    queue = []

    visited.append(node)
    queue.append(node)

    while queue:
      
        v = queue.pop(0)
        print(v, end=" ")

        for neigh in graph[v]:
            if neigh not in visited:
                visited.append(neigh)
                queue.append(neigh)

bfs('A')


# In[20]:


import random

# generate 10 unique random numbers between 1 and 1000
nums = random.sample(range(1, 1000), 10)
print(nums)


# In[23]:


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
        
    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._insert(val, self.root)
            
    def _insert(self, val, node):
        if val < node.val:
            if node.left is None:
                node.left = Node(val)
            else:
                self._insert(val, node.left)
        else:
            if node.right is None:
                node.right = Node(val)
            else:
                self._insert(val, node.right)

# create a binary search tree for the first set of inputs
bst = BST()
for num in nums:
    bst.insert(num)


# In[25]:


def bfs(tree):
    if tree.root is None:
        return
    
    queue = []
    visited = set()
    queue.append(tree.root)
    visited.add(tree.root)
    
    while queue:
        curr = queue.pop(0)
        if curr.left is not None and curr.left not in visited:
            queue.append(curr.left)
            visited.add(curr.left)
        if curr.right is not None and curr.right not in visited:
            queue.append(curr.right)
            visited.add(curr.right)
            
        if len(visited) == total_len - 220:
            return curr.val


# In[29]:


def dfs(tree):
    if tree.root is None:
        return
    
    stack = []
    visited = set()
    stack.append(tree.root)
    visited.add(tree.root)
    
    while stack:
        curr = stack.pop()
        if curr.left is not None and curr.left not in visited:
            stack.append(curr.left)
            visited.add(curr.left)
        if curr.right is not None and curr.right not in visited:
            stack.append(curr.right)
            visited.add(curr.right)
            
        if len(visited) == total_len - 220:
            return curr.val


# In[30]:


import time

start_time = time.time()
bfs_val = bfs(bst)
end_time = time.time()

print(f"BFS value: {bfs_val}")
print(f"BFS time taken: {end_time - start_time} seconds")


# In[43]:


graph = {
    'A': set(['B', 'S']),
    'B': set(['A']),
    'S': set(['A','C','G']),
    'C': set(['D','E','F','S']),
    'G': set(['F','H','S']),
    'D': set(['C']),
    'E': set(['C', 'H']),
    'F': set(['C', 'G']),
    'H': set(['E', 'G'])
}


# In[44]:


def dfs(graph, start):
    visited = set()  # set to keep track of visited nodes
    stack = [start]  # stack for DFS traversal
    while stack:
        vertex = stack.pop()  # get the next vertex from the stack
        if vertex not in visited:
            visited.add(vertex)  # mark the vertex as visited
            stack.extend(graph[vertex] - visited)  # add its neighbors to the stack
    return visited


# In[45]:


dfs(graph, 'A') 


# In[56]:


#DFS IMPLEMENTATION IN GRAPHS


# In[66]:


graph = {
    'A': set(['B', 'S']),
    'B': set(['A']),
    'S': set(['A','C','G']),
    'C': set(['D','E','F','S']),
    'G': set(['F','H','S']),
    'D': set(['C']),
    'E': set(['C', 'H']),
    'F': set(['C', 'G']),
    'H': set(['E', 'G'])
}

visited=set()
def dfs(visited,graph,root):
    if root not in visited:
        print(root)
        visited.add(root)
        for neighbour in graph[root]:
            dfs(visited,graph,neighbour)

   
dfs(visited,graph,'A')


# In[ ]:




