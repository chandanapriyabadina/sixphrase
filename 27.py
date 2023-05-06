from itertools import combinations
def subsetsum (n,arr,x):
    for i in range(n+1):
        for subset in combinations(arr,i):
            if sum (subset)==x:
                print(list(subset))
                n=6
                arr=[10,20,25,50,70,90]
                x=80
                subsetsum[n,arr,x]
