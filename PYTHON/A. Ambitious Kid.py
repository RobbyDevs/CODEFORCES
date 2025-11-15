n = int(input())

v = list(map(int,input().split()))
m = 1000000
for i in v:
    if abs(i) < m:
        m = abs(i)
print(m)