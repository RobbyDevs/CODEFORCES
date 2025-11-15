n,m = map(int,input().split())

v = list(map(int,input().split()))

v.sort()

s = 0
for i in range(m):
    if v[i] < 0:
        s +=v[i]


print(-s if s<0 else 0)