n,m = map(int,input().split())

v = list(map(int,input().split()))

v = sorted(v)
c = 0
for i in range(m):
    if v[i] < 0:
        c+= v[i]
    else:
        break

print(abs(c))