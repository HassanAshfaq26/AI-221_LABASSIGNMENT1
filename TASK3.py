#!/usr/bin/env python
# coding: utf-8

# In[1]:


# TASK 3 VISUALIZATION USING THE BINARY TREE LIBRARY


# In[2]:


from binarytree import tree, bst, heap

# Generate a random binary tree and return its root node.
my_tree = tree(height=3, is_perfect=False)

# Generate a random BST and return its root node.
my_bst = bst(height=3, is_perfect=True)

# Generate a random max heap and return its root node.
my_heap = heap(height=3, is_max=True, is_perfect=False)

# Pretty-print the trees in stdout.
print(my_tree)


# In[3]:


from binarytree import build

# Build a tree from list representation
values = [60,15,75,10,25,70,80,5,12,23,26,None,None,77,92,None,None,None,None,21,None,None,30]
root = build(values)
print(root)


# In[4]:


from binarytree import Node

root = Node(60)
root.left = Node(15)
root.right = Node(75)
root.left.left = Node(10)
root.left.right = Node(25)
root.left.left.left = Node(5)
root.left.left.right = Node(12)
root.left.right.left = Node(23)
root.left.right.right = Node(26)
root.left.right.left.left = Node(21)
root.left.right.right.right = Node(30)
root.right.left = Node(70)
root.right.right = Node(80)
root.right.right.left = Node(77)
root.right.right.right = Node(92)

print(root)


# In[5]:


pip install anytree


# In[6]:


from anytree import Node, RenderTree
udo = Node("Udo")
marc = Node("Marc", parent=udo)
lian = Node("Lian", parent=marc)
dan = Node("Dan", parent=udo)
jet = Node("Jet", parent=dan)
jan = Node("Jan", parent=dan)
joe = Node("Joe", parent=dan)


# In[7]:


print(udo)
print(joe)


# In[8]:


for pre, fill, node in RenderTree(udo):
   print("%s%s" % (pre, node.name))


# In[10]:


from anytree import Node,RenderTree


# In[11]:


A= Node("A")
B=Node("B",parent=A)
C=Node("C",parent=A)
D=Node("D",parent=B)
E=Node("E",parent=B)
F=Node("F",parent=C)
G=Node("G",parent=C)
H=Node("H",parent=D)
I=Node("I",parent=D)
J=Node("J",parent=E)
K=Node("K",parent=E)
L=Node("L",parent=G)
M=Node("M",parent=G)
N=Node("N",parent=J)
O=Node("O",parent=K)


# In[12]:


print(RenderTree(A))


# In[13]:


from anytree.exporter import DotExporter


# In[ ]:


pip install graphviz


# In[15]:


pip install python-graphviz


# In[ ]:


from anytree.exporter import DotExporter


# In[ ]:


from anytree import Node, RenderTree
udo = Node("Udo")
marc = Node("Marc", parent=udo)
lian = Node("Lian", parent=marc)
dan = Node("Dan", parent=udo)
jet = Node("Jet", parent=dan)
jan = Node("Jan", parent=dan)
joe = Node("Joe", parent=dan)


# In[ ]:


print(udo)
print(joe)


# In[ ]:


for pre, fill, node in RenderTree(udo):
       print("%s%s" % (pre, node.name))



# In[2]:


from anytree import Node, RenderTree
udo = Node("Udo")
marc = Node("Marc", parent=udo)
lian = Node("Lian", parent=marc)
dan = Node("Dan", parent=udo)
jet = Node("Jet", parent=dan)
jan = Node("Jan", parent=dan)
joe = Node("Joe", parent=dan)


# In[3]:


print(udo)
print(joe)


# In[4]:


for pre, fill, node in RenderTree(udo):
    print("%s%s" % (pre, node.name))
   


# In[18]:


pip install graphviz


# In[6]:


from anytree.exporter import DotExporter


# In[7]:


DotExporter(udo).to_picture("udo.png")


# In[10]:


pip install treelib


# In[11]:


from treelib import Node, Tree
tree = Tree()
tree.create_node("Harry", "harry")  # root node
tree.create_node("Jane", "jane", parent="harry")
tree.create_node("Bill", "bill", parent="harry")
tree.create_node("Diane", "diane", parent="jane")
tree.create_node("Mary", "mary", parent="diane")
tree.create_node("Mark", "mark", parent="jane")
tree.show()


# In[12]:


from treelib import Node, Tree
tree = Tree()
tree.create_node("A", "A")  # root node
tree.create_node("B", "B", parent="A")
tree.create_node("C", "C", parent="A")
tree.create_node("D", "D", parent="B")
tree.create_node("E", "E", parent="B")
tree.create_node("F", "F", parent="C")
tree.create_node("G", "G", parent="C")
tree.create_node("H", "H", parent="D")
tree.create_node("I", "I", parent="D")
tree.create_node("J", "J", parent="E")
tree.create_node("K", "K", parent="E")
tree.create_node("L", "L", parent="G")
tree.create_node("M", "M", parent="G")
tree.create_node("N", "N", parent="J")
tree.create_node("O", "O", parent="K")
tree.show()


# In[1]:


import turtle   


# In[2]:


ttl = turtle.Turtle()    


# In[16]:


screen=turtle.Screen()


# In[ ]:




