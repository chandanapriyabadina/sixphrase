def lis(nums):
    tails=[0]*len(nums)
    size=0
    for x in nums:
        i,j=0,size
        while i!=j:
            m=(i+j)
            if tails[m]x:
                i=m+1
                else:
                    j=m
                    tails[i]=x
                    size=max(i+1,size)
                    return size
                arr=[10,22,9,33,21,50,41,60,80]
                print=(lis(arr))
