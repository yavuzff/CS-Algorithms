#Merge sort - O(nlogn)

def mergeSort(x):
    if len(x) <= 1: #base case, and empty or single element lists returns itself 
        return x

    mid = len(x)//2
    left = mergeSort(x[:mid])   #each half is merge sorted
    right = mergeSort(x[mid:])

    x = merge(left,right)       #the halves are merged in order

    return x

def merge(a,b):
    c = []  #c is the output list
    low1 = 0 #pointers to the lowest element of each sublist
    low2 = 0

    while low1<len(a) and low2<len(b): #loops until all elements of 1 sublist is merged
        if a[low1] < b[low2]: #checks which element is lower
            c.append(a[low1]) #the lower value element is inserted
            low1 += 1         #the pointer is incremented
            
        else:
            c.append(b[low2])
            low2 += 1

    if low1 == len(a): #checks which sublist is already inserted
        c += b[low2:]  #the rest of the other sublist is added
    else:
        c += a[low1:]
        
    return c
