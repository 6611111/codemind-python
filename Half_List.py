n=int(input())
lst=list(map(int,input().split()))
m=n//2
for i in range(n-1,m-1,-1):
    print(lst[i],end=" ")
for i in range(m):
    print(lst[i],end=" ")