#insertion sort, O(n^2), space complexity O(1)
def insertion(items):

    for i in range(1,len(items)): #loops through all elements except first one
        currentItem = items[i]
        previous = i-1

        while previous >= 0 and currentItem < items[previous]:
        #loops until element is greater than element before or is the first element

            items[previous+1] = items[previous] #moves other elements up the list
            previous = previous -1

        items[previous+1] = currentItem #current item placed at correct index
        
    return items


print(insertion([5,2,4,90,1,6,8]))
