l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
a=0
b=0
for i in range(len(l1)):
    if l1[i]>l2[i]:
        a=a+1
    elif l1[i]<l2[i]:
        b=b+1
print(a,b)