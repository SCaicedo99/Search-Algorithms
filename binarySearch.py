def binarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = False

    while first<=last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1

    return found

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
#print(binarySearch(testlist, 3))
#print(binarySearch(testlist, 13))

def binarySearchRecursive(alist, item):
    first = 0
    last = len(alist)-1
    found = False
    midpoint = (first + last)//2
    if alist[first] == item or alist[last] == item or alist[midpoint] == item:
        return True
    if not alist[first] == item and not alist[last] == item and len(alist) == 2:
        return False
    else:
        lefthand = alist[0:midpoint]
        righthand = alist[midpoint: len(alist)]
        if item < alist[midpoint]:
            found = binarySearchRecursive(lefthand,item)
        else:
            found = binarySearchRecursive(righthand,item)
    return found

print(binarySearchRecursive(testlist,2))
print(binarySearchRecursive(testlist,3))
print(binarySearchRecursive(testlist,42))
print(binarySearchRecursive(testlist,0))

#IF you want to see how long the function takes use timit .. see notes
