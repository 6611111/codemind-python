s=input()
st=s.split()
l1=[]
i=0
while i<len(st):
    l1.append(st[i][::-1])
    i=i+1
op=' '.join(l1)
print(op)