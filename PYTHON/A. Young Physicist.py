n = int(input())
h = v1 = 0
v = []
va = []
for i in range(n):
    v.append(list(map(int,input().split())))

for i in range(3):
    v1=0
    for j in range(n):
        v1+= v[j][i]
    va.append(v1)

for i in va:
    if i!=0:
        print("NO")
        break
    
    
else:
    print('YES')