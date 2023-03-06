#!/usr/bin/env python
# coding: utf-8

# In[1]:


# TASK 2


# In[6]:


import numpy as np


# In[10]:


import matplotlib.pyplot as plt


# In[2]:


class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data

   def insert(self, data):
      if self.data:
         if data < self.data:
            if self.left is None:
               self.left = Node(data)
            else:
               self.left.insert(data)
         elif data > self.data:
               if self.right is None:
                  self.right = Node(data)
               else:
                  self.right.insert(data)
      else:
         self.data = data

   def PrintTree(self,val):
      if self.data==val:
         return
      if self.left:
         self.left.PrintTree(val)
      if self.right:
         self.right.PrintTree(val)
    
   def bfs(self,val):
        queue = []
        queue.append(self)
        while len(queue) > 0:
           current_node = queue.pop(0)
           if current_node.data==val:
              return
           if current_node.left is not None:
              queue.append(current_node.left)
           if current_node.right is not None:
              queue.append(current_node.right)


# In[3]:


import random
import time

list_of_ranges=[1000,40000,80000,100000,200000]
dfs=[]
for k in range(0,4):
   inputList=[]
   for i in range(list_of_ranges[k],list_of_ranges[k+1]):
      inputList.append(i)
   random.shuffle(inputList)
   data_entry=Node(inputList[0])
   for i in range(1,998):
      if i==780:
         num=inputList[i]
      data_entry.insert(inputList[i])
   start=time.time()
   data_entry.PrintTree(num)
   end=time.time()
   dfs.append(start-end)
print(dfs)

BFST=[]
for k in range(0,4):
   inputList=[]
   for i in range(list_of_ranges[k],list_of_ranges[k+1]):
      inputList.append(i)
   random.shuffle(inputList)
   data_entry=Node(inputList[0])
   for i in range(1,998):
      if i==780:
         num=inputList[i]
      data_entry.insert(inputList[i])
   start=time.time()
   data_entry.bfs(num)
   end=time.time()
   BFST.append(start-end)
print(BFST)

