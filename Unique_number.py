n=int(input())
z=0
o=0
t=0
th=0
f=0
fi=0
s=0
se=0
e=0
ni=0
while n!=0:
    if n%10==0:
        z=z+1
    elif n%10==1:
        o=o+1
    elif n%10==2:
        t=t+1
    elif n%10==3:
        th=th+1
    elif n%10==4:
        f=f+1
    elif n%10==5:
        fi=fi+1
    elif n%10==6:
        s=s+1
    elif n%10==7:
        se=se+1
    elif n%10==8:
        e=e+1
    elif n%10==9:
        ni=ni+1
    n=n//10
if z<2 and o<2 and t<2 and th<2 and f<2 and fi<2 and s<2 and se<2 and e<2 and ni<2:
    print("Unique Number")
else:
    print("Not Unique Number")