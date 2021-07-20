#bubble sort, O(n^2) - space complexity O(1)

def bubbleSort(items):
    swap = True #holds whether a swap is made in this pass
    loops = len(items)

    while swap: #loops until no swaps are made
        swap = False

        for i in range(0, loops-1): #loops to the end of the (unsorted) list

            if items[i] > items[i+1]: #makes a swap if previous item is greater
                temp = items[i]
                items[i] = items[i+1]
                items[i+1] = temp
                swap = True

        loops = loops-1
        #we know that the largest element is at swapped to the end of the list

    return items

print(bubbleSort([10,9,4,2,1,5,3,8,7]))
