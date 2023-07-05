s1=input()
s=[]
j=[]
for i in s1:
    c=s1.count(i)
    if c==1: 
        s.append(i)
    elif c>1:
        j.append(i)
if len(s1)==len(j):
    print("-1")
else:
    print(s[0])