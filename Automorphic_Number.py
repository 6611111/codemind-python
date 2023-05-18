n=int(input())
a=str(n)
sq=n*n
b=str(sq)
if b.endswith(a):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")