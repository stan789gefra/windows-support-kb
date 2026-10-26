"""
Practical 8: Practical 8
Description: PageRank Algorithm & Random Walk Simulation (Directed Graphs)
Original File: Prac8.ipynb
"""


# ------------------------------------------------------------
# Q1)
# ------------------------------------------------------------

import networkx as nx
import random
import matplotlib.pyplot as plt
from collections import Counter


#create directed graph
G = nx.DiGraph()
edges=[
    ("A","B"),
    ("A","C"),
    ("B","C"),
    ("B","D"),
    ("C","A"),
    ("C","D"),
    ("D","A"),
    ("D","C")
]

G.add_edges_from(edges)

#VISUALIZE THE NETWORK
nx.draw(G, with_labels=True, node_size=2000,arrows=True)
plt.title("Directed Webpage Network")
plt.show()

#Random Walk
current = 'A'
walk = [current]
random.seed(42)

for _ in range(20):
  neighbours = list(G.successors(current))
  current = random.choice(neighbours)
  walk.append(current)
print("Random Walk:", walk)

#count visits
visit_counts = Counter(walk)
print("Visit Counts:", visit_counts)

for page in G.nodes():
  print(page,":",visit_counts[page])

#PageRank
pagerank = nx.pagerank(G)
print("PageRank:", pagerank)

for page, score in sorted(pagerank.items(), key=lambda x: x[1], reverse=True):
  print(page,":",round(score,4))



# ------------------------------------------------------------
# **the highest pagerank means the higher probability of user staying on that page at the end**
# ------------------------------------------------------------

import networkx as nx
import random
import matplotlib.pyplot as plt
from collections import Counter
random.seed(42)

#create directed graph
G = nx.DiGraph()
edges=[
    ("A","B"),
    ("A","D"),
    ("B","C"),
    ("B","D"),
    ("C","A"),
    ("C","D"),
    ("D","B")

]

G.add_edges_from(edges)

#VISUALIZE THE NETWORK
nx.draw(G, with_labels=True, node_size=2000,arrows=True)
plt.title("Directed Webpage Network")
plt.show()

#Random Walk
current = 'B'
walk = [current]


for _ in range(25):
  neighbours = list(G.successors(current))
  current = random.choice(neighbours)
  walk.append(current)
print("Random Walk:", walk)

#count visits
visit_counts = Counter(walk)
print("Visit Counts:", visit_counts)

for page in G.nodes():
  print(page,":",visit_counts[page])

#PageRank
pagerank = nx.pagerank(G)
print("PageRank:", pagerank)

for page, score in sorted(pagerank.items(), key=lambda x: x[1], reverse=True):
  print(page,":",round(score,4))

