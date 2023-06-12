n=int(input())
lst=list(map(int,input().split()))
s=0
for i in lst:
    if i%2!=0:
        c=i
        break
l=lst.index(c)
for i in range(l):
    s=s+lst[i]
print(s)