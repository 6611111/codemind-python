s=input()
c1=0
c2=0
c3=0
c4=0
for i in s:
    if i.isupper():
        c1=c1+1
    elif i.islower():
        c2=c2+1
    elif i==' ':
        c4=c4+1
    else:
        c3=c3+1
print(c3)