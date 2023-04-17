r,c=map(int,input().split())
s=0
mat=[]
for i in range(r):
    lst=list(map(int,input().split()))
    mat.append(lst)
for i in mat:
    s=s+sum(i)
print(s)
        