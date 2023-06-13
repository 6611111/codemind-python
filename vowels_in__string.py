s=input()
res=[]
c=0
for i in s:
    if i in "AEIOUaeiou":
        if i not in res:
            res.append(i)
            c=c+1
for i in res:
    print(i,end=" ")
if c==0:
    print("-1")