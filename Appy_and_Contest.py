t=int(input())
for i in range(t):
    n,a,b,k=map(int,input().split())
    if(n//a>=k and n//b!=k) or (n//b>=k and n//a!=k):
        print("Win")
    else:
        print("Lose")