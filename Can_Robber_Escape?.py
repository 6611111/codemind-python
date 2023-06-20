n= int(input())
lst=list(map(int,input().split()))
o=0
for i in lst:
    if i%2!=0:
        o=o+1
if o<=2:
    print("YES")
else:
    print("NO")