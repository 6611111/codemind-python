n=int(input())
lst=list(map(int,input().split()))
for i in range(n):
    for j in range(n):
        if(i!=j and lst[i]==lst[j]):
            c=lst[i]
print(c)