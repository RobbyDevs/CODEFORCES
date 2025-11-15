input()
v = list(set(list(map(int,input().split()))))
v.sort()

if len(v)>1:
    print(v[1])
else:
    print("NO")