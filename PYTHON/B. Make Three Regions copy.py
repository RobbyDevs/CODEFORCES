for w in range(int(input())):
    
    n = int(input())
    
    v = []
    
    v.append(input())
    v.append(input())
    #print()
    
    #print(*v,sep='\n')
    

    if n <= 2:
        print(0)
    
    else:
    
        c = 0
        
        for i in range(1,n-1):
            if(v[0][i] == '.' and v[0][i-1] == 'x' and v[0][i+1] == 'x' and v[1][i] == '.' and v[1][i-1] == '.' and v[1][i+1] == '.'):
                c+=1
                
            if(v[1][i] == '.' and v[1][i-1] == 'x' and v[1][i+1] == 'x' and v[0][i] == '.' and v[0][i-1] == '.' and v[0][i+1] == '.'):
                c+=1
            
        print(c)
            