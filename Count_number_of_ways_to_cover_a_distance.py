def cd(n):
    if n<0:
        return 0;
    elif n==0:
        return 1
    else:
        return cd(n-1)+cd(n-2)+cd(n-3)
n=int(input())
r=cd(n)
print(r)