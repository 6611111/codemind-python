n=int(input())
lst=list(map(int,input().split()))
a=sum(lst)
while(n):
    if a%n==0:
        print(n)
        break
    n=n-1