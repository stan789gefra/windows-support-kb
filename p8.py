#====================================================================
# Practical 8: Practical 8: PageRank Algorithm & Random Walk on Graphs
#====================================================================

# --- [Network 1] Simulate Random Walk & Compute PageRank on 4-Node Web Graph ---
import networkx as nx
import random
import matplotlib.pyplot as plt
from collections import Counter

# Set random seed
random.seed(42)

# Create directed graph
G1 = nx.DiGraph()
edges_1 = [
    ("A", "B"), ("A", "C"),
    ("B", "C"), ("B", "D"),
    ("C", "A"), ("C", "D"),
    ("D", "A"), ("D", "C")
]
G1.add_edges_from(edges_1)

# Visualize Graph
plt.figure(figsize=(7, 5))
pos = nx.spring_layout(G1, seed=42)
nx.draw(G1, pos, with_labels=True, node_color='#38bdf8', node_size=2000, 
        font_size=14, font_weight='bold', arrows=True, arrowsize=20, edge_color='#64748b')
plt.title("Network 1: Directed Webpage Network")
plt.show()

# 2. Simulate Random Walk of 20 steps starting at page 'A'
current = 'A'
walk = [current]
for _ in range(20):
    neighbours = list(G1.successors(current))
    current = random.choice(neighbours)
    walk.append(current)

print("Random Walk Sequence (20 steps):", walk)

# 3. Count visits
visit_counts = Counter(walk)
print("\nVisit Counts during Random Walk:")
for page in sorted(G1.nodes()):
    print(f"Page {page}: {visit_counts[page]} visits")

# 4. Compute PageRank
pagerank_1 = nx.pagerank(G1, alpha=0.85)
print("\n--- Stationary PageRank Scores ---")
for page, score in sorted(pagerank_1.items(), key=lambda x: x[1], reverse=True):
    print(f"Page {page}: {score:.4f} ({score*100:.2f}%)")


# --- [Network 2] PageRank on Alternative Web Topology (25-Step Walk from 'B') ---
import networkx as nx
import random
import matplotlib.pyplot as plt
from collections import Counter

random.seed(42)

# Create second directed graph topology
G2 = nx.DiGraph()
edges_2 = [
    ("A", "B"), ("A", "D"),
    ("B", "C"), ("B", "D"),
    ("C", "A"), ("C", "D"),
    ("D", "B")
]
G2.add_edges_from(edges_2)

# Simulate 25-step random walk starting at 'B'
current = 'B'
walk_2 = [current]
for _ in range(25):
    neighbours = list(G2.successors(current))
    current = random.choice(neighbours)
    walk_2.append(current)

print("Random Walk Sequence (25 steps):", walk_2)

# Count visits
visit_counts_2 = Counter(walk_2)
print("\nVisit Counts during Random Walk:")
for page in sorted(G2.nodes()):
    print(f"Page {page}: {visit_counts_2[page]} visits")

# Compute PageRank
pagerank_2 = nx.pagerank(G2, alpha=0.85)
print("\n--- Stationary PageRank Scores ---")
for page, score in sorted(pagerank_2.items(), key=lambda x: x[1], reverse=True):
    print(f"Page {page}: {score:.4f} ({score*100:.2f}%)")

