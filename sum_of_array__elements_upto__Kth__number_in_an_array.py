n=int(input())
lst=list(map(int,input().split()))
k=int(input())
l=lst.index(k)
s=0
for i in range(l+1):
    s=s+lst[i]
print(s)