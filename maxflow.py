from collections import deque

def compute_max_flow(capacity, s, t):
    """
    Args:
    -  capacity: a dictionary {(from,to):edge_capacity, ...}
    -  s, t: the source and sink vertices
    Returns a triple  (flow_value, flow, cutset)  where:
    -  flow_value: the value of the flow, i.e. a number
    -  flow: a dictionary {(from,to):flow_amount, ...}
    -  cutset: a list or set of vertices
    """

    flow = {}
    residual = {}
    graph = {}
    maxflow = 0
    for u,v in capacity:
        #add relationship to adjacency list, needed to check outgoing edges as well as incoming decreasing edges
        graph[u] = graph.get(u,[]) + [v]
        graph[v] = graph.get(v,[]) + [u]

        flow[(u,v)] = 0                         #intialise flow to 0
        residual[(u,v)] = (capacity[(u,v)],0)   #store (how much you can increase by, how much decrease by)

    path = find_augmenting_path(graph, residual, s, t)

    while path[0]: #while there exists an augmenting path

        delta = float('inf')
        v = t
        for i in range (0, len(path[1])):
            info = path[1][i] #stores (previous, inc/dec)
            u = info[0]

            if info[1] == 'inc':
                delta = min(delta, residual[(u,v)][0]) #since increasing, we check edge from u to v
            else:
                delta = min(delta, residual[(v,u)][1]) #since decreasing, this is an edge v,u

            v = info[0]

        #delta found
        v = t
        for i in range (0, len(path[1])):
            info = path[1][i] #stores (previous, inc/dec)
            u = info[0]

            if info[1] == 'inc':
                #update the edge to store new possible increases/decreases
                residual[(u,v)] = (residual[(u,v)][0] - delta, residual[(u,v)][1] + delta)
                flow[(u,v)] += delta
            else:
                #update the edge to store new possible increases/decreases (other way around since this was decreasing)
                residual[(v,u)] = (residual[(v,u)][0] + delta, residual[(v,u)][1] - delta)
                flow[(v,u)] -= delta
            v = info[0]

        maxflow += delta
        path = find_augmenting_path(graph, residual, s,t)

    cut = path[1] #path[1] is the set of visited vertices (i.e. source side of the cut)

    return maxflow,flow,cut

def find_augmenting_path(graph, residual, s, t):
    queue = deque()
    prev = {}
    visited = set()

    queue.append(s)
    visited.add(s)
    prev[s] = (None,'') #prev, increase or decrease
    u = s

    while queue:
        u = queue.popleft()
        if u == t: #if target node found end search
            break

        for v in graph[u]: #for every neighbour of v (either incoming or outgoing)

            if v not in visited:
                if (u,v) in residual and residual[(u,v)][0] > 0: #increasing edge
                    queue.append(v)
                    prev[v] = (u,'inc')
                    visited.add(v)

                elif (v,u) in residual and residual[(v,u)][1] > 0: #decreasing edge
                    queue.append(v)
                    prev[v] = (u,'dec')
                    visited.add(v)

    if u == t:
        #backtrace to produce path
        path = []
        previous = prev[u]
        while previous[0] is not None:
            path.append(previous)
            previous = prev[previous[0]]

        #returns flag to show there is an augmenting path,
        # and sequence of (node, inc/dec) not including the target node at the start
        return True,path

    else: #the target node cannot be reached
        return False, visited #returns set of nodes that can be visited from source
