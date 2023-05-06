def binary.search(lst,item):
    low=0
    high=len(lst)-1
    while low c=high:
        mid=round((low+high))2]
        if lst[mid]==item:
            return mid
        elif lst[mid]>item
        high=mid-1
        else:
            low=mid+1
            return none
        lst=[1,3,5,7]
        print(binary_search(lst,a))
