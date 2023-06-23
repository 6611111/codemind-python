t=int(input())
for i in range(t):
    l=[]
    n=int(input())
    lst=list(map(int,input().split()))
    for j in range(1,n+1):
        l.append(j)
    for j in l:
        for j in lst:
            l.remove(j)
    for i in l:
        print(i)