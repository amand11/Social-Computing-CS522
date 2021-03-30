import networkx as nx
import random

def analyze_network(G):
    num_node = len(G.nodes())
    num_edges = len(G.edges())
    sumd = 0
    avg_clustering = nx.average_clustering(G)
    for (i,j) in G.degree():
        sumd+=j
    avg_deg = sumd/(len(G.nodes()))

    print("Number of Nodes", num_node)
    print("Number of Edges", num_edges)
    print("Average Degree", avg_deg)
    print("Average Clustering", avg_clustering)


def add(G):
    v1 = random.choice(list(G.nodes()))
    v2 = random.choice(list(G.nodes()))
    while v1 == v2 and (v1, v2) not in G.edges():
        v1 = random.choice(list(G.nodes()))
        v2 = random.choice(list(G.nodes()))
    G.add_edge(v1, v2)


def find_num_edges(n):
    node_num = 0
    G = nx.Graph()
    G.add_nodes_from(range(n))
    while not nx.is_connected(G):
        add(G)
        node_num+=1
    return node_num


def edge_remove(G):
    dict1 = nx.edge_betweenness_centrality(G)
    list_tup = []
    for i in dict1:
        k = (i, dict1[i])
        list_tup.append(k)
    list_tup.sort(key=lambda x:x[1], reverse=True)
    return list_tup[0][0];



def find_num_comm(G):
    c = nx.connected_components(G)
    l = len(list(c))
    if l > 1:
        print("Number of Communities ",l)
    else:
        while l == 1:
            G.remove_edge(*edge_remove(G))
            c = nx.connected_components(G)
            l = len(list(c))
        print("Number of Communities ", l)



