t=int(input())
for i in range(t):
    s=input()
    r=s[::-1]
    if(r==s):
        l=len(r)
        if(l%2==0):
            print("YES EVEN")
        elif(l%2!=0):
            print("YES ODD")
    else:
        print("NO")