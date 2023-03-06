#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# TASK 4 APPLYING UCS 


# In[25]:


graph={
    'S':[('A',2),('B',3),('D',5)],
    'A':[('C',4)],
    'B':[('D',4)],
    'C':[('D',1),('G',2)],
    'D':[('G',5)],
    
}


# In[26]:


def path_cost(path):
    total_cost=0
    for (node, cost) in path:
        total_cost +=cost
        return total_cost,path[-1][0]


# In[27]:


path=[('S',0),('O', 5),('G',5)]
print(path_cost(path))


# In[28]:


def ucs (graph,start,goal):
    visited=[]
    queue=[[(start,0)]]
    while queue:
        queue.sort(key=path_cost)
        path=queue.pop(0)
        node=path[-1][0]
        if node in visited:
            continue
            visited.appended(node)
            if node==goal:
               return path
        else:
            adjacent_nodes=graph.get(node,[])
            for (node2,cost) in adjacent_nodes:
                new_path=path.copy()
                new_path.append((node2,cost))
                queue.append(new_path)


# In[22]:


solution=ucs(graph,'S','G')
print(solution)
print(path_cost(solution)[0])


# In[35]:


class Graph:
    def __init__(self):
        self.edges={"Arad":["Zerind","Timisoara","Sibiu"],"Zerind":["Oradea"],"Oradea":["Sibiu"],"Timisoara":["Lugoj"],"Lugoj":["Mehadia"],"Mehadia":["Dobreta"],"Dobreta":["Craiova"],"Sibiu":["Fagaras","RimnicuVilcea"],"Craiova":["RimnicuVilcea","Pitesti"],"RimnicuVilcea":["Craiova","Pitesti"],"Fagaras":["Bucharest"],"Pitesti":["Bucharest"],"Bucharest":["Giurgiu","Urziceni"],"Urziceni":["Hirsova","Vaslui"],"Hirsova":["Eforie"],"Vaslui":["Lasi"],"Lasi":["Neamt"]}
        self.weights={"AradZerind":75,"ZerindOradea":71,"AradTimisoara":118,"TimisoaraLugoj":111,"LugojMehadia":70,"MehadiaDobreta":75,"AradSibiu":140,"OradeaSibiu":151,"DobretaCraiova":120,"CraiovaRimnicuVilcea":146,"CraiovaPitesti":138,"SibiuFagaras":99,"SibiuRimnicuVilcea":80,"RimnicuVilceaPitesti":97,"RimnicuVilceaCraiova":146,"FagarasBucharest":211,"PitestiBucharest":101,"BucharestGiurgiu":90,"BucharestUrziceni":85,"UrziceniHirsova":98,"HirsovaEforie":86,"UrziceniVaslui":142,"VasluiLasi":92,"LasiNeamt":87}
    def neighbors(self,node):
        return self.edges[node]
    def get_cost(self,from_node,to_node):
        return self.weights[(from_node + to_node)]



def ucs(graph, start, goal):
    global total_cost
    visited = set()
    path=[]
    queue = PriorityQueue()
    queue.put((0, start))
    while queue:
        cost, node = queue.get()
        if node not in visited:
            visited.add(node)
            if node == goal:
                return visited
            for i in graph.neighbors(node):
                if i not in visited:
                    total_cost = cost + graph.get_cost(node, i)
                    queue.put((total_cost, I))


graph=Graph()
s=ucs(graph,"Arad","Bucharest")
print(s)


# In[ ]:




