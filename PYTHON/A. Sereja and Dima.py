n = int(input())

v = list(map(int,input().split()))

va = []
vb = []
vez = 0
while len(v)>=1:
    if vez%2==0:
        if v[0]>v[-1]:
            va.append(v[0])
            v.pop(0)
        else:
            va.append(v[-1])
            v.pop(-1)
    else:
        if v[0]>v[-1]:
            vb.append(v[0])
            v.pop(0)
        else:
            vb.append(v[-1])
            v.pop(-1)
    vez+=1
print(sum(va),sum(vb))