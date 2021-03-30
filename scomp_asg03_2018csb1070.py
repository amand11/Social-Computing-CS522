#Social Computing CS522
#Programming Assignment #3
#(Submission Deadline: 8th October 2020)

#Note: The functions given in the assignment are entirely based on the video lectures related to Schelling Model We will be using the same example grid graph. For further details you can refer the related videos. 



import networkx as nx
import matplotlib.pyplot as plt
import random as rd

#Creating grid graph
def create_graph(N):
    return nx.grid_2d_graph(N, N)

#Adding diagonal edges
def add_diagonal_edges(G, N):
    for (u, v) in G.nodes():
        if (u+1 <= N-1) and (v+1 <= N-1):
            G.add_edge((u, v), (u+1, v+1))

    for (u, v) in G.nodes():
        if (u+1 <= N-1) and (v-1 >= 0):
            G.add_edge((u, v), (u+1, v-1))
    return


#Assigning Type to every node as either 0,1 or 2
def assign_type(G):
    for n in G.nodes():
        G.nodes[n]['type'] = rd.randint(0, 2)

#Returns boundary nodes as well as internal nodes of the grid graph, do not print simply return two list of nodes, first should be
#list of boundary nodes and other should be list of internal nodes
def get_boundary_internal_nodes(G,N):
    #Your code
    boundary_node_list = []
    for ((u, v), d) in G.nodes(data = True):
        if u == 0 or u == N-1 or v == 0 or v == N-1:
           boundary_node_list.append((u, v))
#           print(u, v, 'appended')
    internal_nodes_list = list(set(G.nodes()) - set(boundary_node_list) )
    return boundary_node_list,internal_nodes_list



def make_a_node_satisfied(unsatisfied_nodes_list, empty_cells):
    if(len(unsatisfied_nodes_list)!=0):
        node_to_shift = random.choice(unsatisfied_nodes_list)
        new_position = random.choice(empty_cells)
        
        G.nodes[new_position]['type'] = G.node[node_to_shift]['type']
        G.node[node_to_shift]['type'] = 0
        labels[node_to_shift], labels[new_position] = labels[new_position], labels[node_to_shift]
    else:
        pass
        
        

def get_neigh_for_internal(u, v):
    return [(u-1, v), (u+1, v), (u, v-1), (u, v+1), (u-1, v+1), (u+1, v-1), (u-1, v-1), (u+1, v+1)]

def get_neigh_for_boundary(u, v, N):
    if u == 0 and v == 0:
        return [(0, 1), (1, 1), (1, 0)]
    elif u == N-1 and v == N-1:
        return [(N-2, N-2), (N-1, N-2), (N-2, N-1)]
    elif u == N-1 and v == 0:
        return [(u-1, v), (u, v+1), (u-1, v+1)]
    elif u == 0 and v == N-1:
        return [(u+1, v), (u+1, v-1), (u, v-1)]
    elif u == 0:
        return [(u, v-1), (u, v+1), (u+1, v), (u+1, v-1), (u+1, v+1)]
    elif u == N-1:
        return [(u-1, v), (u, v-1), (u, v+1), (u-1, v+1), (u-1, v-1)]
    elif v == N-1:
        return [(u, v-1), (u-1, v), (u+1, v), (u-1, v-1), (u+1, v-1)]
    elif v == 0:
        return [(u-1, v), (u+1, v), (u, v+1), (u-1, v+1), (u+1, v+1)]
        

    
#Returns only the number of unsatisfied nodes out of all the given nodes in the graph, and not the list of all those nodes, where G is a graph of size N*N and t is the threshold for deciding satisfiability of the node.
def num_unsatified_nodes_list(G,N,t):
    #Your Code
    unsatisfied_nodes_list = []
    t = 3
    boundary_nodes,internal_nodes=get_boundary_internal_nodes(G,N)
    for u, v in G.nodes():
        type_of_this_node = G.nodes[(u, v)]['type']
        if type_of_this_node == 0:
            continue
        else:
            similar_nodes = 0
            if (u, v) in internal_nodes:
                neigh = get_neigh_for_internal(u, v)
            elif (u, v) in boundary_nodes:
                neigh = get_neigh_for_boundary(u, v, N)
            
            for each in neigh:
                if G.nodes[each]['type'] == type_of_this_node:
                    similar_nodes+=1
                    
            if similar_nodes <=t:
                unsatisfied_nodes_list.append((u,v))
    
    number_of_unsatisfied_nodes = len(unsatisfied_nodes_list)
    return number_of_unsatisfied_nodes

#Please print your entry number, for example replace <Entry number> by 2014csz0001
print('2018csb1070')

#Test Case 1 where N=5 and t=2 
N = 5
t=2
print('Test Case 1')
G=create_graph(N)
add_diagonal_edges(G, N)
assign_type(G)
boundary_nodes,internal_nodes=get_boundary_internal_nodes(G,N)
print('num_boundary_nodes=',len(boundary_nodes))
print('num_internal_nodes=',len(internal_nodes))
print('num_unsatified_nodes=',num_unsatified_nodes_list(G,N,t))

'''
##Expected Output
Test Case 1
num_boundary_nodes= 16
num_internal_nodes= 9
num_unsatified_nodes= 10
'''
#Test Case 2 where N=10 and t=5
N = 10
t=5
print('Test Case 2')
G=create_graph(N)
add_diagonal_edges(G, N)
assign_type(G)
boundary_nodes,internal_nodes=get_boundary_internal_nodes(G,N)
print('num_boundary_nodes=',len(boundary_nodes))
print('num_internal_nodes=',len(internal_nodes))
print('num_unsatified_nodes=',num_unsatified_nodes_list(G,N,t))

'''
##Expected Output
Test Case 2
num_boundary_nodes= 36
num_internal_nodes= 64
num_unsatified_nodes= 68
'''



#Test Case 3 where N=15 and t=4
N = 15
t=4
print('Test Case 3')
G=create_graph(N)
add_diagonal_edges(G, N)
assign_type(G)
boundary_nodes,internal_nodes=get_boundary_internal_nodes(G,N)
print('num_boundary_nodes=',len(boundary_nodes))
print('num_internal_nodes=',len(internal_nodes))
print('num_unsatified_nodes=',num_unsatified_nodes_list(G,N,t))

'''
##Expected Output
Test Case 3
num_boundary_nodes= 56
num_internal_nodes= 169
num_unsatified_nodes= 128
'''

#Test Case 4 where N=20 and t=7
N = 20
t=7
print('Test Case 4')
G=create_graph(N)
add_diagonal_edges(G, N)
assign_type(G)
boundary_nodes,internal_nodes=get_boundary_internal_nodes(G,N)
print('num_boundary_nodes=',len(boundary_nodes))
print('num_internal_nodes=',len(internal_nodes))
print('num_unsatified_nodes=',num_unsatified_nodes_list(G,N,t))

'''
##Expected Output
Test Case 4
num_boundary_nodes= 76
num_internal_nodes= 324
num_unsatified_nodes= 268
'''

##Kindly note your output values may vary due to randomness
##You may use other functions but make sure I would be directly running your .py file on terminal and no marks will be provided for any kind of errors

'''
Important Notes: 
1)Your file should be named as scomp_asg03_<Your entry number>.py. For example if your entry number is 2014csz0001, your file name should be scomp_asg03_2014csz0001.py. (use only small letters)
2) Make sure you do not copy the code neither from internet nor from any other student.
3) Strictly follow the guidelines given regarding the unimplemented functions and use only Python3.
4) No marks will be given in case of syntactical errors, logical errors of any kind.
5) Your .py file will be executed directly on the command prompt or terminal, so do take care of that.
'''
    
