s=input()
st=s.split()
l1=[]
i=0
while i<len(st):
    if i%2==0:
        l1.append(st[i][::-1])
    else:
        l1.append(st[i])
    i=i+1
op=' '.join(l1)
print(op)