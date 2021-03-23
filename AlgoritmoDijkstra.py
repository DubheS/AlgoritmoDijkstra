#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
# Importando algunas librerías que utilizaremos

# Networkx para grafos
import networkx as nx

# Pandas
import pandas as pd

# Mostrar imágenes
from IPython.display import HTML

# Mathplotlib
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')
plt.rcParams['figure.figsize'] = (20.0, 10.0)


# In[2]:


aero = pd.read_csv('aero.csv')
aero.head()


# In[3]:


aero.set_index(["codigo"], inplace=True)
aero.head()


# In[4]:


aero.loc["MEX"]


# In[5]:


vuelos = pd.read_csv("vuelos.csv")
vuelos.head()


# In[6]:


vuelos.describe()


# In[7]:


DG=nx.DiGraph()
for row in vuelos.iterrows():
    DG.add_edge(row[1]["origen"],
                row[1]["destino"],
                distancia=row[1]["distancia"],
                tiempo=row[1]["tiempo"])


# In[8]:


DG.nodes(data=True)


# In[9]:


nx.draw_circular(DG,
                 node_color="lightblue",
                 edge_color="gray",
                 font_size=24,
                 width=2, with_labels=True, node_size=3500,
)


# In[10]:


list(nx.all_shortest_paths(DG, source="JKF", target="ABC", weight=None))


# In[11]:


list(nx.all_shortest_paths(DG, source="BUD", target="SAL", weight=None))


# In[12]:


list(nx.all_shortest_paths(DG, source="CCC", target="AEP", weight=None))


# In[13]:


list(nx.all_shortest_paths(DG, source="CCC", target="ABC", weight=None))


# In[14]:


list(nx.dijkstra_path(DG, source="CCC", target="ABC", weight="distancia"))


# In[15]:


list(nx.dijkstra_path(DG, source="CCC", target="ABC", weight="tiempo"))


# In[16]:


def show_path(path):
    total_tiempo = 0
    total_distancia = 0
    
    for i in range(len(path)-1):
        origen = path[i]
        destino = path[i+1]
        distancia = DG[origen][destino]["distancia"]
        tiempo = DG[origen][destino]["tiempo"]
        
        total_tiempo = total_tiempo+tiempo
        total_distancia = total_distancia+distancia
        print("    %s -> %s\n    - Distancia: %s Tiempo: %s minutos" % (
            aero.loc[origen]["pais"],
            aero.loc[destino]["pais"],
            distancia, tiempo)
        )
    
    print("\n     Total Distancia: %s Total Tiempo: %s minutos \n" % (
            total_distancia, total_tiempo)
    )


# In[17]:


show_path(['CCC', 'LIM', 'SAL', 'ABC'])


# In[18]:


def get_all_shortest_paths(DiGraph, origen, destino):
    print("*** All shortest paths - Origen: %s Destino: %s" % (
        origen, destino
    ))
    for weight in [None, "distancia", "tiempo"]:
        print("* Ordenando por: %s" % weight)
        paths = list(nx.all_shortest_paths(DiGraph,
                                          source=origen,
                                          target=destino,
                                          weight=weight))
        for path in paths:
            print("   Camino óptimo: %s" % path)
            show_path(path)


# In[19]:


def get_all_shortest_paths(DiGraph, origen, destino):
    print("*** All shortest paths - Origen: %s Destino: %s" % (
        origen, destino
    ))
    for weight in [None, "distancia", "tiempo"]:
        print("* Ordenando por: %s" % weight)
        paths = list(nx.all_shortest_paths(DiGraph,
                                          source=origen,
                                          target=destino,
                                          weight=weight))
        for path in paths:
            print("   Camino óptimo: %s" % path)
            show_path(path)
    


# In[20]:


get_all_shortest_paths(DG, origen="CCC", destino="ABC")


# In[21]:


def plot_shortest_path(path):
    print(path)
    positions = nx.circular_layout(DG)
    
    nx.draw(DG, pos=positions,
                node_color='lightblue',
                edge_color='gray',
                font_size=24,
                width=1, with_labels=True, node_size=3500, alpha=0.8
           )
    
    short_path=nx.DiGraph()
    for i in range(len(path)-1):
        short_path.add_edge(path[i], path[i+1])
    
    nx.draw(short_path, pos=positions,
                node_color='dodgerblue',
                edge_color='dodgerblue',
                font_size=24,
                width=3, with_labels=True, node_size=3000
           )
    plt.show()
        


# In[22]:


def get_shortest_path(DiGraph, origen, destino):
    print("*** Origen: %s Destino: %s" % (origen, destino))
    
    for weight in [None, "distancia", "tiempo"]:
        print(" Ordenado por: %s" % weight)
        path = list(nx.astar_path(DiGraph,
                                  (origen),
                                  (destino),
                                  weight=weight
                                 ))
        print("   Camino óptimo: %s " % path)
        show_path(path)
        plot_shortest_path(path)


# In[23]:


get_shortest_path(DG, origen="CCC", destino="ABC")


# In[24]:


path = ['CCC', 'ABC']
plot_shortest_path(path)


# In[25]:


# https://en.wikipedia.org/wiki/Dijkstra's_algorithm
print("Dijkstra's algorithm")
HTML('<img src="https://upload.wikimedia.org/wikipedia/commons/2/23/Dijkstras_progress_animation.gif">')


# In[ ]:




