n,k = map(int,input().split())

v = [x for x in range(1,n+1,2)]

va = [x for x in range(2,n+1,2)]

v.extend(va)

print(v[k-1])