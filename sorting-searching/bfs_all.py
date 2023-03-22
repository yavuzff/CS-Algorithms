from collections import deque

#find all shortest paths between s and t given graph g (adjacency list)
def shortest_paths(g,s,t):
    q = deque()
    visited = dict() #set of visited nodes with distance
    previous = {}

    q.append((s,0))
    visited[s] = 0
    previous[s] = []

    while len(q) > 0:
        current,dist = q.popleft()

        for neighbour in g[current]:

            if neighbour not in visited:
                previous[neighbour] = [current]
                q.append((neighbour,dist+1))
                visited[neighbour] = dist+1
            else:
                if dist+1 == visited[neighbour]:
                    previous[neighbour].append(current)

    paths = []
    def generatepaths (t,s,path):
        if t not in previous:
            return
        elif t == s:
            paths.append([s] + path)
        else:
            for p in previous[t]:
                generatepaths(p,s,[t]+path)


    generatepaths(t,s,[])

    return paths
