s=input()
v=['a','e','i','o','u','A','E','I','O','U']
c=0
l1=[]
for i in s:
    if i in v:
        l1.append(i)
print(len(l1))
