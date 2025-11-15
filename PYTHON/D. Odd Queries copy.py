for w in range(int(input())):
    n, q = map(int, input().split())
    
    v = list(map(int, input().split()))
    pref = [0]
    
    for i in v:
        pref.append(pref[-1] + (i % 2 != 0))
    
    #print(pref)
    
    Tim = pref[-1]
    
    for vez in range(q):
        l, r, k = map(int, input().split())
        impar = Tim
        l -= 1
        r -= 1
        
        if k %2 == 0:
            impar -= pref[r + 1] - pref[l]
            
        else:
            par = (r-(l-1)) - pref[r + 1] - pref[l]
            impar+= par
        
            
        #print("impares l-r:", impar)
        if impar % 2 == 0:
            print('NO')
        else:
            print('YES')
