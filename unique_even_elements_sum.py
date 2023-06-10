n=int(input())
lst=list(map(int,input().split()))
res_l=[]
for i in lst:
    if i not in res_l:
        res_l.append(i)
s=0
for i in res_l:
    if i%2==0:
        s=s+i
print(s)