ct = int(input())
for _ in range(ct):
    n = int(input())

    v = list(map(int,input().split()))

    while True:

        for i in range(len(v)):
            if v[i+1] > v[i]:
                pass