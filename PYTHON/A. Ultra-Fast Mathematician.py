va = input()
vb = input()

l = len(va)
vc = []
for i in range(l):
    if vb[i] != va[i]:
        vc.append(1)
    else:
        vc.append(0)
print(*vc,sep='')