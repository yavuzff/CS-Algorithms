
import collections

def breadthFirst(start):
    
    queue = collections.deque()
    queue.append(start)
    traversed = []
    
    while queue:
        current = queue.popleft()

        for neighbour in graph[current]:
            if neighbour not in traversed and neighbour not in queue:
                queue.append(neighbour)
        traversed.append(current)
        #print(traversed)
        
    return traversed

graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : ['A'],
  'E' : ['F'],
  'F' : []
}
start = 'A'

print(breadthFirst(start))
