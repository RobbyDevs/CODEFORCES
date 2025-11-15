n,p = map(int,input().split())

v = list(map(int,input().split()))
c = 0
for i in v:
    if i >= v[p-1] and i >0:
        c+=1
        
print(c)