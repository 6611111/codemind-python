s=input()
v="aeiou"
c=0
a=0
for i in range(len(s)):
    if s[i] in v:
        c+=1
        a=max(a,c)
    else:
        c=0
print(a)