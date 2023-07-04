n=int(input())
w=[]
for i in range(n):
    n1=int(input())
    w.append(n1)
t=int(input())
a=0
for i in w:
    a+=1
    if(i>t):
        a+=1
print(a)