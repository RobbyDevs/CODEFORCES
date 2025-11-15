n = int(input())

for _ in range(n):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = int(input())

    if n == 1:
        print("YES")
        continue

    a[0] = min(a[0], b - a[0])

    for i in range(1, n):
        if min(a[i], b - a[i]) >= a[i-1]:
            a[i] = min(a[i], b - a[i])
        else:
            a[i] = max(a[i], b - a[i])

    flag = True
    for i in range(1, n):
        if a[i] < a[i-1]:
            flag = False
            break
    
    print("YES") if flag else print("NO")
        