for w in range(int(input())):
    
    n,m = map(int,input().split())
    
    if m>n:
        print('NO')
    elif m == n:
        print('YES')
        
        
    else:
        
        if n == 3*m:
            print('YES')
        else:
            v = []
            val = n
            while val > m:  
                v.append(val*(2/3))
                v.append(val*(1/3))
                val = val*(2/3)
                
        #print(v)
            
            for i in range(len(v)):
                if v[i] == m or m == v[i]/3:
                    print('YES')
                    break
            else:
                print('NO')