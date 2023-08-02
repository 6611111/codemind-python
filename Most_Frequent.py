n=int(input())
lst=list(map(int,input().split()))
r=max(set(lst),key=lst.count)
print(r)