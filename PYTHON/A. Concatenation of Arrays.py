ct = int(input())

for i in range(ct):
    n = int(input())
    a = []
    for i in range(n):

        a += list(map(int,input().split()))
    
    a = [str(i) for i in a]
    print(" ".join(a))