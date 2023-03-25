# Fibonacci Heap

class FibHeap:

    class Node:
        def __init__(self,v,k):
            self.v = v
            self.k = k
            self.parent = None
            self.right = self
            self.left = self
            self.child = None
            self.loser = False
            self.degree = 0


    def __init__(self):
        self.nodes = {}
        self.minp = None


    def push(self, x, k):
        if x in self.nodes:
            raise ValueError(f"Item {x} is already in heap")
        n = FibHeap.Node(x,k)
        self.nodes[x] = n
        
        if self.minp is None: # first node in the heap
            self.minp = n
        else:
            FibHeap.__insert(self,n)
            
    def __insert(self,n):
        r = self.minp.right
        n.right = r
        n.left = self.minp
        self.minp.right = n
        r.left = n

        if n.k < self.minp.k:
            self.minp = n
        
    def __removeSubnode(self,n):
        n.parent.degree -= 1
        if n.right == n: #only child
            n.parent.child = None
        else:
            n.parent.child = n.right
            n.right.left = n.left
            n.left.right = n.right
        n.parent = None
        
    def decreasekey(self, x, k):
        if x not in self.nodes:
            raise KeyError(f"Item {x} not in heap")
        n = self.nodes[x]
        n.k = k

        if n.parent is None:
            # if it is already a root node
            if self.minp.k > k:
                self.minp = n
                
        elif n.parent.k > k:
            #bring this node to the root list
            
            p = n.parent
            FibHeap.__removeSubnode(self,n)
            FibHeap.__insert(self,n)
            n.loser = False
            n = p

            while p.loser:
                p = n.parent
                FibHeap.__removeSubnode(self,n)
                FibHeap.__insert(self,n)
                n.loser = False
                n = p

            if p.parent is not None:
                p.loser = True

    def popmin(self):
        if self.minp is None:
            raise IndexError("Heap is empty.")

        del self.nodes[self.minp.v]
        value = self.minp.v
        
        if self.minp.child is None:
            if self.minp.right == self.minp: # this was only node in the heap
                self.minp = None
                return value
            
            else:
                # remove the node from the root list
                self.minp.right.left = self.minp.left
                self.minp.left.right = self.minp.right
                self.minp = self.minp.right  # temporarily set minp, will be updated at the end
        else:

            #mark children as non losers and remove their parent
            first = self.minp.child
            curr = first
            curr.parent = None
            curr.loser = False
            while curr.right != first:
                curr = curr.right
                curr.parent = None
                curr.loser = False
            
            # promote children to root
            if self.minp.right != self.minp: # if this isnt the only node
                # combine two circular doubly linked lists
                h1 = first
                t1 = first.left
                h2 = self.minp.right # removes minp
                t2 = self.minp.left
                
                t1.right = h2
                h2.left = t1
                t2.right = h1
                h1.left = t2

            self.minp = first        # temporary

        FibHeap.__cleanuproots(self)
        return value

    def __cleanuproots(self):
        # precondition: there is at least 1 root
        roots = {}
        trees = []

        # add the roots to a list
        start = self.minp
        trees.append(start)
        current = start
        while current.right != start:
            current = current.right
            trees.append(current)

            if current.k < self.minp.k: # update minp to correct value
                self.minp = current

        for t in trees:
            x = t
            while roots.get(x.degree, None) is not None: # while there already is a tree of that degree
                u = roots[x.degree]
                roots[x.degree] = None

                # merge u and x which are both roots
                x = FibHeap.__mergeroots(self,x,u)

            roots[x.degree] = x

    def __mergeroots(self,s,t):

        if s.k <= t.k:
            p = s
            c = t
        else:
            p = t
            c = s

        #remove child from root list
        c.right.left = c.left
        c.left.right = c.right
        
        c.parent = p
        p.degree += 1

        # add child to children of p
        if p.child is None:
            p.child = c
            c.left = c
            c.right = c
        else:
            c.right = p.child.right
            c.left = p.child
            p.child.right = c
            c.right.left = c

        if p.k <= self.minp.k: #if parent and child have the same key, ensure the parent is minp
            self.minp = p

        return p
        
    def __bool__(self):
        return len(self.nodes) == 0

    def __contains__(self, x):
        return x in self.nodes

    def displaystate(self):
        print("minpointer:", self.minp.v if self.minp is not None else None)
        print("object, key, parent, left, right, child, loser, degree")
        for k,v in self.nodes.items():
            print(f"""{k}: {v.k}, {v.parent if v.parent is None else v.parent.v}, {v.left if v.left is None else v.left.v}, {v.right if v.right is None else v.right.v}, {v.child if v.child is None else v.child.v}, {v.loser}, {v.degree}""")
