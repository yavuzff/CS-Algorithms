# Bellman ford algorithm
# returns distances from source vertex to rest,
# or a negative weight cycle reachable from s

def bf(g,s):
    # g is adjacency dictionary {v:{u:1,...}...}
    # returns dict of distance to each vertex, None or if there is a cycle: None, [u,...,u]
    distance = {v:float('inf') for v in g}
    distance[s] = 0
    prev = {}

    for i in range (0,len(g) - 1): # relax each edge every iteration
        # loop over every edge
        for u in g:
            for v in g[u]:
                #u reachable, v unvisited yet or shorter path
                if distance[u] + g[u][v] < distance[v]:
                    distance[v] = distance[u] + g[u][v] # update new distance
                    prev[v] = u

    # loop once more to see if any distance decreases - if so there is a negative edge cycle
    for u in g:
        for v in g[u]:
            if distance[u] + g[u][v] < distance[v]:
                # cycle found
                cycle = []
                current = v
                visited = {} # stores index in cycle of each vertex

                # loop until a vertex is repeated
                while current not in visited:
                    cycle.append(current)
                    visited[current] = len(cycle) - 1
                    current = prev[current]

                # extract and reverse to get cycle
                cycle = cycle[visited[current]:] + [current]
                cycle.reverse()

                return None, cycle

    return distance, None
