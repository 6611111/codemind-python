def unique(s):
    from collections import Counter
    c=Counter(s)
    for i,j in enumerate(s):
        if c[j]==1:
            return i
    else:
        return -1
s=input()
r=unique(s)
print(r)