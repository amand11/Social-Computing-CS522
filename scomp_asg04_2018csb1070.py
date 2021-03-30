#Social Computing CS522
#Programming Assignment #4
#(Submission Deadline: 15th October 2020)

#Note: The functions given in the assignment are entirely based on the video lectures related to Point Distribution Method for Implementing Page Rank. For further details you can refer the related videos. 

#If there is any query related to assignment you should ask at least 48 hours before the deadline, no reply would be given in case you ask during the last 48 hours.
#Please avoid asking any syntax related queries, if you feel anything given can lead to an error, you may change it but make sure the desired output does not change.


import networkx as nx
import random
import numpy as np

#Creating empty graph, adding 'N' nodes and some edges based on the probability 'p'
def create_graph(N,p):
    G = nx.DiGraph()#empty graph
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
                
def initialize_points(G):
    points = [100 for i in range(G.number_of_nodes())]
    return points



#Implement the function for distribution of points by each node to its outlinks
def distribute_points(G, points):
   #Your code goes here
    prev_points = points
    new_points = [0 for i in range(G.number_of_nodes())]
    
    for i in G.nodes():
        out = G.out_edges(i)
        if len(out) == 0:
            new_points[i] += prev_points[i]
        else:
            share = (float)(prev_points[i])/len(out)
            for each in out:
                new_points[each[1]] += share
                
    return G, new_points



##Implement the function for handling the case of sink nodes by collecting 20% of points from each node as given in video lectures
def handle_points_sink(G, points):
    #Your code goes here
    for i in range(len(points)):
        points[i] = (float)(points[i])*0.8
    
    n = G.number_of_nodes()
    extra = ((float)(n)*100*0.2)/n
    for i in range(len(points)):
        points[i] += extra
    return points



def keep_distibuting_points(G, points):
    prev_points = points
    iter=1
    no_change=0
    while(no_change==0 and iter<=100):
        G, new_points = distribute_points(G, prev_points)
        #print(new_points)
        
        ##
        new_points = handle_points_sink(G, new_points)
        new_points=[round(pt,4) for pt in new_points]
        
        
        if prev_points==new_points:
            no_change=1
        prev_points = new_points 
        iter+=1
    if no_change==1:
        print('Total iterations = ',iter)
    else:
        print('Total iterations = ',iter-1)
    return G, new_points



#Returns the sorted nodes based on the points in descending order 
def get_nodes_sorted_by_points(points):
    points_array = np.array(points)
    nodes_sorted_by_points = np.argsort(-points_array)
    
    return nodes_sorted_by_points
 

#Please print your entry number, for example replace <Entry number> by 2014csz0001, Kindly do not delete this statement.
print('2018csb1070')

# Test Case 1 with N=5 and p=0.3
print('Test Case 1')
N=5
p=0.3
G=create_graph(N,p)

# Assign 100 points to each node.
points = initialize_points(G)
    
# Keep distributing points until convergence.
G, points = keep_distibuting_points(G, points)
    
# Get nodes' raking as per the points accumulated
nodes_sorted_by_points = get_nodes_sorted_by_points(points)
print('Nodes sorted by Points Distribution Method : ', ' '.join(map(str,nodes_sorted_by_points)))
    
# Compare the ranks thus obtained with the ranks obtainrd from the inbuilt Page rank method
pr = nx.pagerank(G)# Return a dictionary
pr_sorted = sorted(pr.items(), key = lambda x:x[1], reverse = True)

inbuilt_node_list=[]
for i in pr_sorted:
    inbuilt_node_list.append(i[0])

print('Nodes sorted by Inbuilt Page Rank Method: ',' '.join(map(str,inbuilt_node_list)))

'''
##Expected Output
Test Case 1
Total iterations =  28
Nodes sorted by Points Distribution Method :  4 1 0 3 2
Nodes sorted by Inbuilt Page Rank Method:  4 1 0 3 2

'''

# Test Case 2 with N=10 and p=0.3
print('Test Case 2')
N=10
p=0.3
G=create_graph(N,p)

# Assign 100 points to each node.
points = initialize_points(G)
    
# Keep distributing points until convergence.
G, points = keep_distibuting_points(G, points)
    
# Get nodes' raking as per the points accumulated
nodes_sorted_by_points = get_nodes_sorted_by_points(points)
print('Nodes sorted by Points Distribution Method : ', ' '.join(map(str,nodes_sorted_by_points)))
    
# Compare the ranks thus obtained with the ranks obtainrd from the inbuilt Page rank method
pr = nx.pagerank(G)# Return a dictionary
pr_sorted = sorted(pr.items(), key = lambda x:x[1], reverse = True)

inbuilt_node_list=[]
for i in pr_sorted:
    inbuilt_node_list.append(i[0])

print('Nodes sorted by Inbuilt Page Rank Method: ',' '.join(map(str,inbuilt_node_list)))


'''
##Expected Output
Test Case 2
Total iterations =  15
Total iterations =  21
Nodes sorted by Points Distribution Method :  6 2 4 8 7 1 0 3 5 9
Nodes sorted by Inbuilt Page Rank Method:  6 2 4 8 7 1 0 3 5 9

'''

# Test Case 3 with N=20 and p=0.5
print('Test Case 3')
N=20
p=0.5
G=create_graph(N,p)

# Assign 100 points to each node.
points = initialize_points(G)
    
# Keep distributing points until convergence.
G, points = keep_distibuting_points(G, points)
    
# Get nodes' raking as per the points accumulated
nodes_sorted_by_points = get_nodes_sorted_by_points(points)
print('Nodes sorted by Points Distribution Method : ', ' '.join(map(str,nodes_sorted_by_points)))
    
# Compare the ranks thus obtained with the ranks obtainrd from the inbuilt Page rank method
pr = nx.pagerank(G)# Return a dictionary
pr_sorted = sorted(pr.items(), key = lambda x:x[1], reverse = True)

inbuilt_node_list=[]
for i in pr_sorted:
    inbuilt_node_list.append(i[0])

print('Nodes sorted by Inbuilt Page Rank Method: ',' '.join(map(str,inbuilt_node_list)))

'''
##Expected Output
Test Case 3
Total iterations =  14
Nodes sorted by Points Distribution Method :  2 9 8 7 10 14 4 3 17 0 16 6 11 1 18 15 19 5 13 12
Nodes sorted by Inbuilt Page Rank Method:  2 9 8 7 10 14 4 3 17 0 16 6 11 1 18 15 19 5 13 12

'''

##Kindly note your output values may vary due to randomness.
##You may use other functions but make sure I would be directly running your .py file on terminal and no marks will be provided for any kind of errors.
## Kindly do not add any additional print statements other than given in the code.


'''
Important Notes: 
1)Your file should be named as scomp_asg04_<Your entry number>.py. For example if your entry number is 2014csz0001, your file name should be scomp_asg04_2014csz0001.py. (use only small letters)
2) Make sure you do not copy the code neither from internet nor from any other student.
3) Strictly follow the guidelines given regarding the unimplemented functions and use only Python3.
4) No marks will be given in case of syntactical errors, logical errors of any kind.
5) Your .py file will be executed directly on the command prompt or terminal, so do take care of that.

'''
    
