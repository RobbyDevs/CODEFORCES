from math import ceil

for w in range(int(input())):

    x,y,k = map(int,input().split())
        
    x1 = ceil(x/k)
    y1 = ceil(y/k)

    s1 = abs(x1-y1)
    if x1 > y1:
        x1 -=1
    print(x1 + y1 + s1)