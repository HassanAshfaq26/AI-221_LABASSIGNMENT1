#!/usr/bin/env python
# coding: utf-8

# In[4]:


pip install binarytree


# In[5]:


pip install --upgrade pip


# In[6]:


class Node:

    def __init__(self, value, left=None, right=None):
        self.value = value  # The node value (float/int/str)
        self.left = left    # Left child
        self.right = right  # Right child


# In[7]:


from binarytree import tree, bst, heap

# Generate a random binary tree and return its root node.
my_tree = tree(height=3, is_perfect=False)

# Generate a random BST and return its root node.
my_bst = bst(height=3, is_perfect=True)

# Generate a random max heap and return its root node.
my_heap = heap(height=3, is_max=True, is_perfect=False)

# Pretty-print the trees in stdout.
print(my_tree)


# In[13]:


# Creating node class
class Node:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

# Function to insert in BST
    def insert(self, data):
        # if value is lesser than the value of the parent node
        if data < self.data:
            if self.leftChild:
                # if we still need to move towards the left subtree
                self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
                return
        # if value is greater than the value of the parent node        
        else:
            if self.rightChild:
                # if we still need to move towards the right subtree
                self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return

    # function to print a BST
    def PrintTree(self):
        if self.leftChild:
            self.leftChild.PrintTree()
        print( self.data),
        if self.rightChild:
            self.rightChild.PrintTree()

# Creating root node
root = Node(27)
# Inserting values in BST
root.insert(14)
root.insert(35)
root.insert(31)
root.insert(10)
root.insert(19)
# printing BST
root.PrintTree()


# In[27]:


from binarytree import build

# Build a tree from list representation
values = [60,15,75,10,25,70,80,5,12,23,26,None,None,77,92,None,None,None,None,21,None,None,30]
root = build(values)
print(root)


# In[ ]:


from binarytree import Node

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)

