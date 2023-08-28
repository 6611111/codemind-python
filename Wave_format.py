n=int(input())
lst=list(map(int,input().split()))
lst.sort(reverse=True)
for i in range(0,n-1,2):
    lst[i],lst[i+1]=lst[i+1],lst[i]
print(*lst)