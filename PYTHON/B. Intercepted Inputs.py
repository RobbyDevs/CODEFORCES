ct = int(input())
 
for _ in range(ct):
    l = int(input())
    ll = l-2
    v = list(map(int,input().split()))
    v0 = [0]*(l+1)
    vd = []
    for i in v:
        if ll%i == 0:
            if v0[i] == 0:
                vd.append(i)
            v0[i] +=1

    for cand in vd:

        div = ll//cand

        if div == cand and v0[div]>1:
            print(div, cand)
            break

        elif div != cand and v0[div]>=1:
            print(div, cand)
            break

