import re
email=input()
pattern="\d+"
ans=re.findall(pattern,email)
print(ans)
