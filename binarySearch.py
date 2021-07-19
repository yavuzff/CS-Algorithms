#binary search, O(log n), list must be sorted

def binarySearchIter(items,target): #iterative binary search
    found = False
    start = 0 #points to start of the (sub)list to search
    end = len(items)-1 #points to end of the (sub)list to search

    while not found and start <= end: #loops until found or the item is not in the list
        mid = (start + end) // 2 #middle of the sublist calculated

        if items[mid] == target: #found if this is the target
            found = True

        elif items[mid] > target:   #if middle is greater
            end = mid-1             #new sublist is the lower half
 
        else:                       #if middle is less
            start = mid+1           #new sublist is upper half

    if found:
        return mid
    else:
        return -1

def binarySearchRecur(items,s,e,x): #recursive binary search
    if s>e:
        return -1

    mid = (s+e)//2

    if items[mid] == x: #found if this is the target
        return mid
    elif items[mid] > x:   #if middle is greater
        return binarySearchRecur(items,s,mid-1,x) #call itself with new upper bound
    else:                       #if middle is less
        return binarySearchRecur(items,mid+1,e,x) #call itself with new lower bound

    
print(binarySearchRecur([1,2,5,6,8,99],0,5,6))


