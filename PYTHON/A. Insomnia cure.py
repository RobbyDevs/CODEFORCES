k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())
v = [k,l,m,n]
va = []
if k == 1:
    print(d)
else:
    
    for i in v:
        for j in range(1,d+1):
            if j%i == 0:
                va.append(j)

    print(len(list(set(va))))