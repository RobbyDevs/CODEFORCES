def solve():
    alf = 'abcdefghijklmnopqrstuvwxyz'
    
    dic = {}
    for i in range(len(alf)):
        dic[alf[i]] = i+1
    
    n,m = map(int,input().split())
    vs = []
    for i in range(n):
        vs.append(input())
        
    vans = []
    for k in range(len(vs)):
        for j in range(len(vs)):
            if k != j:

                ans = 0
                for i in range(m):
                    ans+= abs(dic[vs[k][i]]-dic[vs[j][i]])
                vans.append(ans)
                
    if vans:
        print(min(vans))
    else: print(0)
for w in range(int(input())):
    solve()