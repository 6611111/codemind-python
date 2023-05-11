st=input()
c=0
for i in st:
    if i.isdigit()==True:
        x=int(i)
        c=c+1
if c>0:
    print(f"Contains {c} digit")
else:
    print("Doesn't contain digit")