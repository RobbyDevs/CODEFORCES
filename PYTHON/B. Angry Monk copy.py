for w in range(int(input())):
    
    n,k = map(int,input().split())
    
    v = list(map(int,input().split()))
    
    count1 = 0
    count2 = 0
    mai = 0
    dif = 1000000
    
    for i in range(k):
        if v[i] == 1:
            count1 +=1
        if v[i] == 2:
            count1 +=1
            
            
        if abs(v[i]-n)<dif:
            mai = v[i]
            dif = abs(v[i]-n)
            
    
    #print(count1,mai)
    
    dif = n-mai
    #print('mai ',mai,"  dif",dif)
    
    
    if mai + count1 == n:
        print(count1)
        
        
    else:
        f = (dif - count1)-count2
        #print('mai>>>',mai)
        #print('f>>',f)
        #print('dif>>>',dif)
        a = dif + f
        print('>>>>',a)
