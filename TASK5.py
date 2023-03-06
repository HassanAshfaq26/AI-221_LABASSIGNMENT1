#!/usr/bin/env python
# coding: utf-8

# In[1]:


# TASK 5


# In[ ]:


import networkx as nx
import matplotlib.pyplot as plt

g=nx.Graph()

g.add_node("Arad",pos=(0.4,0.4))
g.add_edge("Arad","Zarind",pos=(0.4,0.4))
g.add_edge("Arad","Timisoara",pos=(0.4,0.4))
g.add_edge("Arad","Sibiu",pos=(0.4,0.4))
g.add_edge("Arad","Sibiu",pos=(0.4,0.4))
g.add_edge("Zarind","Oradea")
g.add_edge("Timisoara","Lugoj")
g.add_edge("Sibiu","Oradea")
g.add_edge("Sibiu","Fagaras")
g.add_edge("Sibiu","Riminiciu")
g.add_edge("Lugoj","Mehadia")
g.add_edge("Fagaras","Bucharest")
g.add_edge("Riminiciu","Pitesti")
g.add_edge("Riminiciu","Craiova")
g.add_edge("Mehadia","Dobreta")
g.add_edge("Bucharest","Pitesti")
g.add_edge("Bucharest","Girugiu")
g.add_edge("Bucharest","Urzeicni")
g.add_edge("Dobreta","Craiova")
g.add_edge("Urzeicni","Hirsova")
g.add_edge("Urzeicni","Vaslui")
g.add_edge("Eforie","Hirsova")
g.add_edge("Vaslui","lassi")
g.add_edge("lassi","Neamt")

print(nx.info(g))

nx.draw(g,with_labels=True)

plt.show()


# In[ ]:




