def even(x):
    return x%2==0
def squar(x):
    return x*x
li=[1,2,3,4,5,6,7,8,9,10]
li=map(squar:filter(even,li))
print(list(li))
