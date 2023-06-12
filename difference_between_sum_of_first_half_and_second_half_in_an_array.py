n=int(input())
lst=list(map(int,input().split()))
s1=0
s2=0
for i in range(0,n//2):
    s1=s1+lst[i]
for i in range(n//2,n):
    s2=s2+lst[i]
print(abs(s1-s2))