def repition(s,n):
    s_l=len(s)
    p=n//s_l
    r=n%s_l
    return s.count("a")*p+s[:r].count("a")
s=input()
n=int(input())
r=repition(s,n)
print(r)
