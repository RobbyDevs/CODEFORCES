for w in range(int(input())):
    
    n,f,k = map(int,input().split())
    
    v = list(map(int,input().split()))
    
    if k == n:
        print('YES')
        
    else:
        
        ff = v[f-1]
        
        v.sort(reverse= True)
        
        #print(v)
        #print(ff)
        ans = 'NO'
        for i in range(k):
            if v[i] == ff:
                if v[i+1]==ff:
                    ans = "MAYBE"
                    
                else:
                    ans = 'YES'
                    break
        
        print(ans)