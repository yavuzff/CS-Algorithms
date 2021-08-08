#Page Rank algorithm

import numpy as np
import matplotlib.pyplot as plt

manualInput = True

if manualInput:
        print('Enter websites in the form: A B C D ...')
        names = input('> ').split()
        n = len(names)
        
        nameIndex = {}
        for i in range (0,n):
                letter = names[i]
                nameIndex[letter] = i

        links = {}
        for i in names:
                print('Enter outgoing links from '+str(i)+':')
                outgoing = input('> ').split()
                links[i] = outgoing

        print(links)
else:
        names = ['A', 'B', 'C', 'D', 'E', 'F']
        n = 6
        nameIndex = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5}
        links = {'A':['B','C','D'],'B':['A','C'],'C':['A','D','F'],'D':['C'],'E':['B','D'],'F':['C','D']}


rankVector = np.ones(n)/n #generating rank vector length n,
                          #each starting with 1/n probability

#Generating linkMatrix
linkMatrix = np.zeros([n,n])
for i in names:
        neighbours = links[i]
        
        if len(neighbours) == 0 or (len(neighbours) == 1 and neighbours[0] == i):
                neighbours = names
                #if a page has no outgoing links to other pages
                #it will be linked to all pages with same probability
                
        probability = 1/len(neighbours) #probability of going from current page to a specific neighbour  
        for j in neighbours:
                linkMatrix[nameIndex[j],nameIndex[i]] = probability #places the value at correct spot in matrix

print(linkMatrix)


#damping factor needed as if a page only links to itself, all of the traffic will go there
d = 0.85 # should be 0.85, or for websites that have no links, link to all websties equally
linkMatrix = d * linkMatrix + (1-d)/n * np.ones([n, n]) # np.ones() is the J matrix, with ones for each entry.


newR = linkMatrix.dot(rankVector)
iterations = 0
while np.linalg.norm(rankVector-newR) > 0.000001: #loops until R converges
        rankVector = newR
        newR = linkMatrix.dot(rankVector)
        iterations += 1
        
rankVector = newR
print(iterations, 'iterations to converge.')


pages = [[round(rankVector[i]*100,4), names[i]] for i in range (0,n)]

pages.sort(reverse=True)
print (pages)

print('Ranking:')
for i in range (0,n):
        print (pages[i][1])


scores = [i[0] for i in pages]
xlabels = [i[1] for i in pages]

plt.bar(xlabels, scores) #bar graph to show rankings
plt.show()
