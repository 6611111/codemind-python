n=int(input())
lst=list(map(int,input().split()))
k=int(input())
c=0
for i in range(len(lst)):
    if lst[i]==k:
        c=1
if c==1:
    print(True)
else:
    print(False)