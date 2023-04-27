str=input("Type in:")
str=list(str)
l,d=0,0
for i in str:
    if i.isalpha():
        l=l+1
    if i.isdigit():
        d=d+1
print("Letters:",l)
print("Digits:",d)
