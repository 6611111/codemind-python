n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
s=0
l=[]
for i in range(n):
    s=a[i]+b[i]
    l.append(s)
    s=0
for i in l:
    print(i,end=" ")