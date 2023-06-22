n=int(input())
lst1=list(map(int,input().split()))
lst2=list(map(int,input().split()))
s1=sum(lst1)
s2=sum(lst2)
if s1>s2:
    print("0")
else:
    print(s2-s1)