#Social Computing CS522
#Programming Assignment #6
#(Submission Deadline: 29th October 2020)

#Note: The functions given in the assignment are entirely based on the video lectures related to Counting Unstable Triangles. For further details you can refer the related videos. 

#If there is any query related to assignment you should ask at least 48 hours before the deadline, no reply would be given in case you ask during the last 48 hours.
#Please avoid asking any syntax related queries, if you feel anything given can lead to an error, you may change it but make sure the desired output does not change.
#Kindly do not delete any test cases given in the program.


import networkx as nx
import random
import itertools

random.seed(30)

#Create an undirected graph with N nodes, make it a complete graph with each edge having an attribute sign with value as '+' or '-'
def complete_graph_signed_edges(N):
    #Your Code goes here
    G = nx.complete_graph(N)
    signs = ['+', '-']
    for i in G.nodes:
        for j in G.nodes:
            if i!=j:
                G.add_edge(i, j, sign = signs[random.randint(0, 1)])
    return G

#Returns the list of triangles in graph G            
def get_tri_list(G):
    #Your Code goes here
    nodes = G.nodes()
    tris_list = [list(x) for x in itertools.combinations(nodes, 3)]
    return tris_list

#Returns all signs of triangles

def get_signs_of_tris(tris_list, G):
    #Your Code goes here
    all_signs = []
    for i in range(len(tris_list)):
        temp = []
        temp.append(G[tris_list[i][0]][tris_list[i][1]]['sign'])
        temp.append(G[tris_list[i][1]][tris_list[i][2]]['sign'])
        temp.append(G[tris_list[i][2]][tris_list[i][0]]['sign'])
        all_signs.append(temp)
    return all_signs

#Returns number of unstable triangles
def count_unstable(all_signs):
    # Your Code goes here
    num_unstable = 0
    for i in range(len(all_signs)):
        if all_signs[i].count('+') == 2 or all_signs[i].count('+') == 0:
            num_unstable+=1
    return num_unstable

#Please print your entry number, for example replace <Entry number> by 2014csz0001, Kindly do not delete this statement.
print('2018csb1070')


#Test Case 1
#Get complete graph with each edge having a sign attribute having value as '+' or '-'
N=5
print('N=',N)
G=complete_graph_signed_edges(N)

                    
# Get list of triangles
tris_list=get_tri_list(G)

#Get the sign details of all the triangles
all_signs = get_signs_of_tris(tris_list, G)

#Get the number of unstable triangles
num_unstable = count_unstable(all_signs)
print('Number of stable traingle out of ', len(tris_list), ' are ', len(tris_list)-num_unstable)
print('Number of unstable traingle out of ', len(tris_list), ' are ', num_unstable)

#Test Case 2
#Get complete graph with each edge having a sign attribute having value as '+' or '-'
N=7
print('N=',N)
G=complete_graph_signed_edges(N)

                    
# Get list of triangles
tris_list=get_tri_list(G)

#Get the sign details of all the triangles
all_signs = get_signs_of_tris(tris_list, G)

#Get the number of unstable triangles
num_unstable = count_unstable(all_signs)
print('Number of stable traingle out of ', len(tris_list), ' are ', len(tris_list)-num_unstable)
print('Number of unstable traingle out of ', len(tris_list), ' are ', num_unstable)

#Test Case 3
#Get complete graph with each edge having a sign attribute having value as '+' or '-'
N=10
print('N=',N)
G=complete_graph_signed_edges(N)

                    
# Get list of triangles
tris_list=get_tri_list(G)

#Get the sign details of all the triangles
all_signs = get_signs_of_tris(tris_list, G)

#Get the number of unstable triangles
num_unstable = count_unstable(all_signs)
print('Number of stable traingle out of ', len(tris_list), ' are ', len(tris_list)-num_unstable)
print('Number of unstable traingle out of ', len(tris_list), ' are ', num_unstable)

#Test Case 4
#Get complete graph with each edge having a sign attribute having value as '+' or '-'
N=20
print('N=',N)
G=complete_graph_signed_edges(N)

                    
# Get list of triangles
tris_list=get_tri_list(G)

#Get the sign details of all the triangles
all_signs = get_signs_of_tris(tris_list, G)

#Get the number of unstable triangles
num_unstable = count_unstable(all_signs)
print('Number of stable traingle out of ', len(tris_list), ' are ', len(tris_list)-num_unstable)
print('Number of unstable traingle out of ', len(tris_list), ' are ', num_unstable)

'''
##Expected Output after running your code
<Entry number>
N= 5
Number of stable traingle out of  10  are  5
Number of unstable traingle out of  10  are  5
N= 7
Number of stable traingle out of  35  are  18
Number of unstable traingle out of  35  are  17
N= 10
Number of stable traingle out of  120  are  60
Number of unstable traingle out of  120  are  60
N= 20
Number of stable traingle out of  1140  are  600
Number of unstable traingle out of  1140  are  540
'''

##You may use other functions but make sure I would be directly running your .py file on terminal and no marks will be provided for any kind of errors.
## Kindly do not add any additional print statements other than given in the code.


'''
Important Notes: 
1)Your file should be named as scomp_asg06_<Your entry number>.py. For example if your entry number is 2014csz0001, your file name should be scomp_asg06_2014csz0001.py. (use only small letters)
2) Make sure you do not copy the code neither from internet nor from any other student.
3) Strictly follow the guidelines given regarding the unimplemented functions and use only Python3.
4) No marks will be given in case of syntactical errors, logical errors of any kind.
5) Your .py file will be executed directly on the command prompt or terminal, so do take care of that.

'''
    
