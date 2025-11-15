n = int(input())

v = list(map(int,input().split()))

if v[0] == max(v) and v[-1] == min(v):
    print(0)
    
else:
    for i in range(n):
        