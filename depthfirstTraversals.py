from collections import deque

def inorder(index):
    global ans1 #global variable used as each recursive call will need to update
    if index == -1: # base case: stop if null pointer
        return
    node = nodes[index] #finds child nodes of current node
    inorder(node[1]) #traverse left child
    ans1 += str(node[0])+' ' # deal with current item
    inorder(node[2]) #traverse right child


def preorder(index):
    global ans2
    if index == -1:
        return
    node = nodes[index]
    ans2 += str(node[0])+' '
    preorder(node[1])
    preorder(node[2])

def postorder(index):
    global ans3
    if index == -1:
        return
    node = nodes[index]
    postorder(node[1])
    postorder(node[2])
    ans3 += str(node[0]) + ' '


def inorderIter(nodes):
    elements = []
    stack = deque() #stack is used
    current = 0 #index of root node
    
    while True: #loops until all elements are dealt with
        if current == -1 and len(stack) == 0:
            return elements #return found elements
        while current != -1: #loops until a leaf is reached
            stack.append(current) #adds all of the nodes on the way to stack
            current = nodes[current][1] #pointer updated to next element

        index = stack.pop() #pointer to bottom leaf retrieved
        info = nodes[index] 
        elements.append(nodes[index][0]) #element added to list
        current = info[2] #current node updated to right child


def preorderIter(nodes):
    answer = ''
    stack = deque()
    stack.append(0)

    while len(stack) > 0:
        current = nodes[stack.pop()]
        answer += str(current[0])+' '

        if current[2] != -1:
            stack.append(current[2])
        if current[1] != -1:
            stack.append(current[1])
        
    return answer.rstrip()

def postorderIter(nodes):
    answer = ''
    stack = deque()

    current = 0
    while True:
        while current != -1:
            info = nodes[current]
            if info[2] != -1:
                stack.append(info[2])
            stack.append(current)
            current = info[1]

        current = stack.pop()
        info = nodes[current]
        if info[2] != -1 and len(stack) >0 and stack[-1] == info[2]:
            temp = stack.pop()
            stack.append(current)
            current = temp
        else:
            answer += str(info[0]) + ' '
            current = -1

        if len(stack) == 0:
            return answer.rstrip()
    
    
nodesCount = int(input())
nodes = {}#for each node: key,left,right

for i in range (0,nodesCount):
    nodes[i] = [int(x) for x in input().split()]

print (inorderIter(nodes) + '\n' + preorderIter(nodes) + '\n' + postorderIter(nodes))

