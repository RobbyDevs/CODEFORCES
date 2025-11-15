def solve():
    t = int(input())
    for _ in range(t):
        x, y, z = map(int, input().split())

        a = b = c = 0
        ok = True

        for bit in range(31):
            X = (x >> bit) & 1
            Y = (y >> bit) & 1
            Z = (z >> bit) & 1

            # testa as combinaes possveis para (X,Y,Z)
            if (X, Y, Z) == (0, 0, 0):
                continue
            elif (X, Y, Z) == (1, 0, 0):   # (a,b,c) = (1,1,0)
                a |= 1 << bit
                b |= 1 << bit
            elif (X, Y, Z) == (0, 1, 0):   # (a,b,c) = (0,1,1)
                b |= 1 << bit
                c |= 1 << bit
            elif (X, Y, Z) == (0, 0, 1):   # (a,b,c) = (1,0,1)
                a |= 1 << bit
                c |= 1 << bit
            elif (X, Y, Z) == (1, 1, 1):   # (a,b,c) = (1,1,1)
                a |= 1 << bit
                b |= 1 << bit
                c |= 1 << bit
            else:
                ok = False
                break

        if ok:
            print("YES")
        else:
            print("NO")


solve()