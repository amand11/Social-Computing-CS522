#Social Computing CS522
#Programming Assignment #7
#(Submission Deadline: 5th November 2020)

#Note: The functions given in the assignment are based on link prediction.

#If there is any query related to assignment you should ask at least 48 hours before the deadline, no reply would be given in case you ask during the last 48 hours.
#Please avoid asking any syntax related queries, if you feel anything given can lead to an error, you may change it but make sure the desired output does not change.
#Kindly do not delete any test cases given in the program.



import pandas as pd
import networkx as nx
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

#Implement the following functions for finding features of each edge

#Compute page rank for all the given nodes in G using inbuilt function
def get_page_rank(G,nodes):
    #Your code
    pr = nx.pagerank(G)
    pr1 = []
    for i in nodes:
        pr1.append(pr[i])

    return pr1

#Find whether there is an edge from B to A, if there is an edge from A to B, for every edge in G
def do_follow_back(G,source_nodes,dest_nodes):
    #Your code
    foll_back = []
    for i in range(len(source_nodes)):
        foll_back.append(G.has_edge(dest_nodes[i], source_nodes[i]))

    return foll_back

#Find the number of followers of each node
def find_num_foll(G,nodes):
    #Your code
    foll_count = []
    for i in nodes:
        foll_count.append(G.in_degree(i))

    return foll_count


#Find the number of followee of each node
def find_num_fole(G,nodes):
    #Your code
    fole_count = []
    for i in nodes:
        fole_count.append(G.out_degree(i))

    return fole_count

#Find the common number of followers for each pair of nodes connected through an edge.
def find_num_comm_foll(G,source_nodes,dest_nodes):
    #Your code
    num_of_source_nodes = len(source_nodes)
    comm_foll_count = []
    for i in range(num_of_source_nodes):
        a1 = set([j for j in G.predecessors(source_nodes[i])])
        a2 = set([j for j in G.predecessors(dest_nodes[i])])
        comm_foll_count.append(len(list(a1 & a2)))

    return comm_foll_count

#Find the common number of followee for each pair of nodes connected through an edge.
def find_num_comm_fole(G,source_nodes,dest_nodes):
    #Your code
    n = len(source_nodes)
    comm_fole_count = []
    for i in range(n):
        a1 = set([j for j in G.successors(source_nodes[i])])
        a2 = set([j for j in G.successors(dest_nodes[i])])
        comm_fole_count.append(len(list(a1 & a2)))

    return comm_fole_count


#Do not make any change in the code given below when submitting it, I will be executing this code on Windows platform , so please take care


#Please print your entry number, for example replace <Entry number> by 2014csz0001, Kindly do not delete this statement.
print('2018csb1070')

#Loading dataset
#The File contains pair of source node and destination node representing an edge, where an edge from A to B means A follows B
#The class assigned as 1 indicates actual edges and 0 as missing edges
df=pd.read_csv(r'graph_link_prediction_dataset.csv')

#Constructing graph
source_nodes=list(df['Source'].values)
dest_nodes=list(df['Destination'].values)
edge_list=list(zip(source_nodes,dest_nodes))
G=nx.DiGraph()
G.add_edges_from(edge_list)
print(nx.info(G))

#Extracting features

#Page Rank
source_pr=get_page_rank(G,source_nodes)
dest_pr=get_page_rank(G,dest_nodes)

#Follows_backs
foll_back=do_follow_back(G,source_nodes,dest_nodes)

#Number of followers
source_foll_count=find_num_foll(G,source_nodes)
dest_foll_count=find_num_foll(G,dest_nodes)

#Number of followee
source_fole_count=find_num_fole(G,source_nodes)
dest_fole_count=find_num_fole(G,dest_nodes)

#Number of common followers and followees
comm_foll_count=find_num_comm_foll(G,source_nodes,dest_nodes)
comm_folle_count=find_num_comm_fole(G,source_nodes,dest_nodes)

df['source_pr']=source_pr
df['dest_pr']=dest_pr
df['foll_back']=foll_back
df['source_foll_count']=source_foll_count
df['dest_foll_count']=dest_foll_count
df['source_fole_count']=source_fole_count
df['dest_fole_count']=dest_fole_count
df['comm_foll_count']=comm_foll_count
df['comm_folle_count']=comm_folle_count

#The below code is for training and testing a machine learning model using the features computed above
#Since this is not a machine learning course, so do not break your head for the below code.
#No paramter tuning or model selection is being done. If you feel you may try for yourself, but make sure you do not change the code as far as assigment submission is concerned.


X=df[['source_pr','dest_pr','foll_back','source_foll_count','dest_foll_count','source_fole_count','dest_fole_count','comm_foll_count','comm_folle_count']].to_numpy()
Y=df[['Class']].to_numpy()

X_train, X_test, Y_train, Y_test  = train_test_split(X, Y, test_size = 0.25, random_state=20)
lr=LogisticRegression(random_state=20,solver='lbfgs')
lr.fit(X_train, Y_train.ravel())
print(confusion_matrix(lr.predict(X_test).ravel(), Y_test.ravel()))

'''
Expected Output
2014csz0014
Name:
Type: DiGraph
Number of nodes: 50107
Number of edges: 70648
Average in degree:   1.4099
Average out degree:   1.4099
[[8495  738]
 [ 250 8179]]
'''


'''
Important Notes:
1)Your file should be named as scomp_asg07_<Your entry number>.py. For example if your entry number is 2014csz0001, your file name should be scomp_asg07_2014csz0001.py. (use only small letters)
2) Make sure you do not copy the code neither from internet nor from any other student.
3) Strictly follow the guidelines given regarding the unimplemented functions and use only Python3.
4) No marks will be given in case of syntactical errors, logical errors of any kind.
5)Please do not submit the csv file, only the template filled with functions code should be submitted
5) Your .py file will be executed directly on the command prompt, so do take care of that.

'''
