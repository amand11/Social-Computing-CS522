import networkx as nx
import random
import numpy as np
from random import randint

random.seed(30)


# Creating empty graph, adding 'N' nodes and some edges based on the probability 'p'
def create_graph(N, p):
    G = nx.DiGraph()  # empty graph
    G.add_nodes_from([i for i in range(N)])
    for i in G.nodes():
        for j in G.nodes():
            if i != j:
                r = random.random()
                if r <= p:
                    G.add_edge(i, j)
                else:
                    continue
    return G


# Returns the sorted nodes based on the points accumulated using random walk in descending order
def get_nodes_sorted_by_RW(points):
    ##Your Code goes here
    points_array = np.array(points)
    nodes_sorted_by_RW = np.argsort(-points_array)
    return nodes_sorted_by_RW


# Returns the points accumulated using random walk executed for 10000 steps, as given in the video lectures
# Returns the points accumulated using random walk executed for 10000 steps, as given in the video lectures
def random_walk(G):
    nodes = G.nodes()
    RW_points = [0 for i in range(G.number_of_nodes())]
    # print(G.nodes())
    r = random.randint(0, G.number_of_nodes())
    # print(r)
    RW_points[r] = RW_points[r] + 1
    out = G.out_edges(r)
    # print(out)
    # print(RW_points)
    c = 0
    while (c != 100000):
        if (len(out) == 0):
            focus = random.randint(0, G.number_of_nodes()-1)
        else:
            # print(out)
            edges = list(G.edges)
            chosen_edge = random.choice(edges)
            focus = chosen_edge[1]
        RW_points[focus] += 1
        out = G.out_edges(focus)
        c += 1

    return RW_points
# Please print your entry number, for example replace <Entry number> by 2014csz0001, Kindly do not delete this statement.
print('2018csb1070')

# Test Case 1 with N=5 and p=0.3
N = 5
p = 0.3

G = create_graph(N, p)
# 2. Perform a random walk
RW_points = random_walk(G)

# 3. Get nodes' raking as per the points accumulated
nodes_sorted_by_rwalk = get_nodes_sorted_by_RW(RW_points)

print('Nodes sorted by Random Walk : ', ' '.join(map(str, nodes_sorted_by_rwalk)))

# 4. Compare the ranks thus obtained with the ranks obtainrd from the inbuilt Page rank method
pr = nx.pagerank(G)  # Return a dictionary
pr_sorted = sorted(pr.items(), key=lambda x: x[1], reverse=True)

inbuilt_node_list = []
for i in pr_sorted:
    inbuilt_node_list.append(i[0])

print('Nodes sorted by Inbuilt Page Rank Method: ', ' '.join(map(str, inbuilt_node_list)))

# Test Case 2 with N=10 and p=0.3
N = 10
p = 0.3

G = create_graph(N, p)
# 2. Perform a random walk
RW_points = random_walk(G)

# 3. Get nodes' raking as per the points accumulated
nodes_sorted_by_rwalk = get_nodes_sorted_by_RW(RW_points)

print('Nodes sorted by Random Walk : ', ' '.join(map(str, nodes_sorted_by_rwalk)))

# 4. Compare the ranks thus obtained with the ranks obtainrd from the inbuilt Page rank method
pr = nx.pagerank(G)  # Return a dictionary
pr_sorted = sorted(pr.items(), key=lambda x: x[1], reverse=True)

inbuilt_node_list = []
for i in pr_sorted:
    inbuilt_node_list.append(i[0])

print('Nodes sorted by Inbuilt Page Rank Method: ', ' '.join(map(str, inbuilt_node_list)))

# Test Case 3 with N=20 and p=0.5
N = 20
p = 0.5

G = create_graph(N, p)
# 2. Perform a random walk
RW_points = random_walk(G)

# 3. Get nodes' raking as per the points accumulated
nodes_sorted_by_rwalk = get_nodes_sorted_by_RW(RW_points)

print('Nodes sorted by Random Walk : ', ' '.join(map(str, nodes_sorted_by_rwalk)))

# 4. Compare the ranks thus obtained with the ranks obtainrd from the inbuilt Page rank method
pr = nx.pagerank(G)  # Return a dictionary
pr_sorted = sorted(pr.items(), key=lambda x: x[1], reverse=True)

inbuilt_node_list = []
for i in pr_sorted:
    inbuilt_node_list.append(i[0])

print('Nodes sorted by Inbuilt Page Rank Method: ', ' '.join(map(str, inbuilt_node_list)))
