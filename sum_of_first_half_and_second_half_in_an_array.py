n=int(input())
lst=list(map(int,input().split()))
s=0
s1=0
for i in range(0,n//2):
    s=s+lst[i]
for i in range(n//2,n):
    s1=s1+lst[i]
print(s)
print(s1)