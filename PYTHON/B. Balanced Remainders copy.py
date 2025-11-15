v = list(map(int,input().split()))


s = sum(v)//3

vs = [v[0] - s, v[1]-s, v[2]-s]
print(vs)

if vs.index(max(vs)) == 0:
    