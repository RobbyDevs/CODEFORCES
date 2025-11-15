for w in range(int(input())):
    
    n = int(input())
    
    vx = list(map(int,input().split()))
    vs = [vx[0]+1]
    
    c = False
    for i in range(n-2):
        
        if vx[i+1] >= vx[i]:
            
            for j in range(vx[i+1]+1, 1000000000):
                if j % vs[i] == vx[i]:
                    vs.append(j)
                    break
        
        #elif vx[i+1] < vx[i]:
        else:
            print(vs)
            for j in range(vs[i]+1,1,-1):
                if j % vs[i] == vx[i]:
                    vs.append(j)
                    break
            else:
                vs.append()
            
    vs.append(vs[len(vs)-1]+vx[len(vx)-1])
    print(vs)
    
    #TLE. TENTAR POR SOMA