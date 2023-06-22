n=int(input())
lst=list(map(int,input().split()))
l=[]
for i in lst:
    a=i**0.5
    if a.is_integer():
        l.append(i)
print(sum(l))