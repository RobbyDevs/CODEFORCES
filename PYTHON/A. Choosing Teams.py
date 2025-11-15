n,k = map(int,input().split())

v = list(map(int,input().split()))
c = r = s = 0
for i in v:
    if i <= 5-k:
        c+=1
        
print(c//3)