#linear search, O(n), list doesnt need to be sorted

def linearSearch(items, target):

    for i in range (0,len(items)): #loops through each item
        if items[i] == target: #if target element found, returns index
            return i

    return -1

def linearSearch2(items,target):
    found = False
    index = 0
    while not found and index < len(items):
        if items[index] == target:
            found = True
        else:
            index += 1

    return Found

print(linearSearch([6,1,2,5,8,9,10],11))
