v = list(map(int,input().split()))
    
v.sort()

print(abs(v[0]-v[1]) + abs(v[1]-v[2]))

