for w in range(int(input())):

    n = int(input())
    vn = map(int,input().split())
    

    nfp = 0
    nfi = 0
    vi = []
    
    for i in vn:
        if i%2!=0:
            vi.append(i)
            
        else:
            nfp += i
            


    if len(vi) == 0:
        print(0)
    else:
        #cortar as impares
        
        vi.sort()
        
        ans = vi[-1]
        vi.pop()
        
        
        ans += nfp
        #print(vi)
        if len(vi) <= 1:
            pass
        elif len(vi) == 2:
            ans+= vi[1]
        elif len(vi) == 3:
            ans+= vi[2]
        
        else:
            if len(vi)%2==0:
                ans+= sum(vi[(len(vi)//2):])
            else:
                ans+= sum(vi[((len(vi)//2)+1):])
        
        print(ans)
            
        
        
        
        