e=int(input())
lst=list(map(int,input().split()))
n=int(input())
ol=[]
if n>len(lst):
    n = int(n%len(lst))
for i in range(len(lst)-n,len(lst)):
    ol.append(lst[i])
for i in range(0,len(lst)-n):
    ol.append(lst[i])
print(*ol)