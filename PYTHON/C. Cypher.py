for w in range(int(input())):
    
    n = int(input())
    
    v = list(map(int,input().split()))
    
    vr = []
    
    for i in range(n):
        s = 0
        
        vi = input().split()
        
        ni = int(vi[0])
        
        for j in vi[1]:
            if j == 'D':
                s+=1
            else:
                s-=1
                
        vr.append(s)
        
    #print(vr)
    
    for i in range(n):
        v[i] = (v[i]+vr[i]) %10
    print(*v,sep=' ')