s=input()
l=s.split()
ll=[]
i=0
while i<len(l):
    ll.append(l[i][::-1])
    i=i+1
op=' '.join(ll)
print(op)