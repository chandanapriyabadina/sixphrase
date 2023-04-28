evtuple=(1,2,3,4,5,6,7,8,9,10)
print("tuple items = ",evtuple)
print("\n the even numbers in this evtuple are:")
for i in range (len(evtuple)):
    if (evtuple[i]%2==0):
        print(evtuple[i],end=" ")
