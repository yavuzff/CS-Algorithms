from collections import deque

class DisjointSet:

    class Node:
        def __init__(self,k):
            self.k = k
            self.parent = self
            self.children = set()
            self.rank = 1

    def __init__(self,keys = []):
        self.nodes = {}
        for k in keys:
            self.nodes[k] = DisjointSet.Node(k)
        
    def add(self, k):
        # Adds a new set consisting of a single item k
        self.nodes[k] = DisjointSet.Node(k)

    def __getitem__(self, k):
        # Returns a handle to the set containing item k
        n = self.nodes[k]
        sub = []
        while n.parent != n:
            sub.append(n)
            n = n.parent
            
        # path compression heuristic
        for i in sub: #update each node along the path to child of parent
            i.parent.children.remove(i) #remove i from its old parent
            i.parent = n
            n.children.add(i) #set used so the child of n is not added a second time to children

        return n.k
        

    def merge(self, h, i):
        # Merge set-with-handle h and set-with-handle i]
        if h == i:
            return
        n1 = self.nodes[h]
        n2 = self.nodes[i]

        # weighted union heuristic
        if n1.rank >= n2.rank:
            n2.parent = n1
            n1.children.add(n2)
            if n1.rank == n2.rank:
                n1.rank += 1
        else:
            n1.parent = n2
            n2.children.add(n1)

    def iter_from(self, k):
        # Returns all items in the subset containing k
        n = self.nodes[k]
        handleNode = self.nodes[self.__getitem__(k)]

        # bfs the tree from this handle
        items = []
        q = deque()
        q.append(handleNode)

        while q:
            current = q.popleft()
            items.append(current.k)
            
            for child in current.children:
                q.append(child)

        return items
