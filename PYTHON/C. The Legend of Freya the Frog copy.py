from math import ceil

for w in range(int(input())):
    
    x,y,k = map(int, input().split())
 
    if ceil(x/k) > ceil(y/k):
        print((2*ceil(x/k))-1)
    else:
        print(2*ceil(y/k))
