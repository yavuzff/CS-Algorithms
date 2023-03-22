#Quicksort - average case O(nlogn) worst case O(n^2)


#optional randomize list first to avoid worst case complexity
#import random
#def sort(x):
#    random.shuffle(x)
#    return quicksort(x)


def quicksort(x):
    if len(x) <= 1:#base case, returns itself if list size 0 or 1
        return x

    pivot = x[0] #pivot is picked as first element
    low = 1      #low and high pointers used
    high = len(x) - 1 #any element at index greater than high is larger than pivot element
    done = False
    
    while not done: #loops until high is less than low
        while low<len(x) and x[low] <= pivot: 
            low += 1 #low is incremented until it reaches a value that is greater than pivot
        while x[high] > pivot:
            high -= 1 #high is decremented until it reaches a value that is lower than pivot

        if low <= high: #if the pointers havent overlapped 
            temp = x[high] #swap values at pointers
            x[high] = x[low]
            x[low] = temp
        else:
            done = True
            #if pointers have overlapped, everything to the left of high marker is
            #less than the pivot and everythign to the right is greater than pivot
            
    x[0] = x[high] #pivot element swapped with element at high
    x[high] = pivot #pivot element is now in its correct final position

    left = quicksort(x[:high]) #left and right of the pivot element is quicksorted
    right = quicksort(x[high+1:])

    return left + [pivot] + right


