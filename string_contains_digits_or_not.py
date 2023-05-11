tc=int(input())
for i in range(tc):
    st=input()
    c=0
    for x in st:
        if x.isdigit()==True:
            y=int(x)
            c=c+1
    if c>0:
        print("Yes")
    else:
        print("No")