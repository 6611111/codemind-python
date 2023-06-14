import math
t=int(input())
for i in range(t):
    n=int(input())
    sq=n**0.5
    if sq.is_integer():
        print("True")
    else:
        print("False")