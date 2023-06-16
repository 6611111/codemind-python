l=int(input())
h=int(input())
for i in range(l,h+1):
    c=0
    q=i
    t=0
    while(q!=0):
        c=c+1
        r=q%10
        if(r!=0 and i%r==0):
            t=t+1
        q=q//10
    if c==t:
        print(i,end=" ")