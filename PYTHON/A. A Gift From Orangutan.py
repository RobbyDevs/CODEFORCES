n = int(input())
for i in range(n):
    len = int(input())
    a = list(map(int,input().split()))
    b = [a[0]]
    c = [a[0]]
    r = 0
    for i in range(len-1):
        b.append(min(a))
        c.append(max(a))

    for i in range(len):
        r += c[i]-b[i]
    
    print(r)