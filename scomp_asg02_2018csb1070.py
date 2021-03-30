import networkx as nx
import matplotlib.pyplot as plt
import  random
import math

def get_persons_nodes(G):
    p = []
    for i in G.nodes():
        if G.nodes[i]['type'] == 'person':
            p.append(i)
    return p

def get_foci_nodes(G):
    f = []
    for i in G.nodes():
        if G.nodes[i]['type'] == 'foci':
            f.append(i)
    return f


def homophily(G):
    ed = [G.number_of_edges()]
    person_node = get_persons_nodes(G)
    for i in person_node:
        for j in person_node:
            if i!=j:
                dif = abs(G.nodes[i]['name'] - G.nodes[j]['name'])
                p = float(1)/(dif+1000)
                r = random.uniform(0, 1)
                if r<p:
                    G.add_edge(i, j)
    ed.append(G.number_of_edges())
    return  ed

def change_bmi(G):
    cnt = 0
    person_node = get_persons_nodes(G)
    for i in person_node:
        if i == 40:
            cnt+=1
    ed = [cnt]
    cnt = 0
    fnd = get_foci_nodes(G)
    for i in fnd:
        if G.nodes[i]['name'] == 'eatout':
            for j in G.G.neighbors(i):
                if G.nodes[j]['name'] != 40:
                    G.nodes[j]['name']+=1

    person_node = get_persons_nodes(G)
    for i in person_node:
        if i == 40:
            cnt += 1
    ed.append(cnt)
    return ed


def cmn(i, j, G):
    nu = set(G.neighbors(i))
    nv = set(G.neighbors(j))
    return len(nu & nv)



def closure(G):
    array1= []
    ed = [G.number_of_edges()]
    for i in G.nodes():
        for j in G.nodes():
            if i!=j and (G.nodes[i]['type'] == 'person' or G.nodes[j]['type'] == 'person'):
                k = cmn(i, j, G)
                p = 1 - math.pow((1-0.1), k)
                tmp = [i, j, p]
                array1.append(tmp)
    for i in array1:
        u = i[0]
        v = i[1]
        p = i[2]
        r = random.uniform(0, 1)
        if r<p:
            G.add_edge(u, v)
    ed.append(G.number_of_edges())
    return ed
