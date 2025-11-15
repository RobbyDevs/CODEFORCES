ct = int(input())

for i in range(ct):
    n = int(input())
    t = [(0) for i in range(0,n-1)]
    t.append(1)
    a = [str(i) for i in t]
    print(''.join(a))