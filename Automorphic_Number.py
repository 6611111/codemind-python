n=int(input())
a=str(n)
sq=n**2
b=str(sq)
if b.endswith(a):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")