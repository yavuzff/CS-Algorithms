#Kruskal's Algorithm for finding the minimum spanning tree of a connected graph

from disjoint_set import DisjointSet #pip install disjoint-set if needed

def kruskal(g):
    #given list of edges (s,t,w), return list of edges that form min span tree

    forest = DisjointSet() #stores trees formed by the chosen edges so far

    #form forest of vertices
    for s,t,_ in g:
        forest.find(s)
        forest.find(t)
        
    #iterate over edges with increasing weight 
    edges = sorted(g,key = lambda x: x[2])

    minspantree = []
    for s,t,w in edges:
        if not forest.connected(s,t):
            forest.union(s,t)
            minspantree.append((s,t,w))

    return minspantree
