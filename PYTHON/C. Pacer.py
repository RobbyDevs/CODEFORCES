for w in range(int(input())):
    n,m = map(int,input().split())
    
    patual = 0
    matual = 0
    ans = 0
    
    for i in range(n):
        
        mi,pi = map(int,input().split())
        
        if patual == pi:
            if mi-matual <2:
                pass
            else:
                ans+= ((mi-matual)//2)*2
            
            matual = mi
        else:
            
            dif = (mi-matual)-1
            ans+=1
            patual = pi
            
            if mi-matual <2:
                pass
            else:
                ans+= (dif//2)*2
            
            matual = mi
        #print("r: ", ans)
    
    print(ans+(m-matual))
  #  print("^^^^")