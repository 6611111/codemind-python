s=input()
st=s.split()
l1=[]
i=len(st)-1
while i>=0:
    l1.append(st[i])
    i=i-1
op=' '.join(l1)
print(op)