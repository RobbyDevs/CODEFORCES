import math

for w in range(int(input())):
    n = int(input())
    v = list(map(int,input().split()))
    print(max(v)-min(v))
    #print()