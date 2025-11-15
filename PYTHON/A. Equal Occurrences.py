def solve():
    n = int(input())
    
    
    v = list(map(int,input().split()))
    
    vc = []
    vf = [0]*(n+1)
    count = 1
    
    ant = v[0]
    vf[v[0]]+=1
    
    for i in range(1,n):
        
        vf[v[i]]+=1
        
        if v[i] == ant:
            count+=1
        
        else:
            vc.append(count)
            count = 1
            ant = v[i]
            
    vc.append(count)
        
    vf.sort()
    #print("vf:",vf)
    ind = 0
    mai =0
    vans = []
    
    
    for i in range(len(vf)):
        ans = vf[i]
        if vf[i] >0:
            for j in range(i,n):
                if vf[j]>0:
                    
                    if vf[j]>=vf[i]:
                        ans+=vf[i]
                        
            vans.append(ans)

    
    #print("vans:",vans)
    print(max(vans))
    
for w in range(int(input())):
    solve()