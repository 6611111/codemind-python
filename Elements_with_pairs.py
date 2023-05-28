n=int(input())
lst=list(input().split())
l1=lst
l=len(lst)
if l%2!=0:
    l1.append('0')
print(' '.join(l1))