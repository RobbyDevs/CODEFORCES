n,h = map(int,input().split())

v = list(map(int,input().split()))
c = n
for i in v:
    if i > h:
        c+=1
print(c)