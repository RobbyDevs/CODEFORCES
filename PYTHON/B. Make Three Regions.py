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
        
        for i in range(n-2):
            if (v[0][i] == 'x'):
                
                if i >0:
                    if (v[1][i-1:i+2] == '..x') or (v[1][i-1:i+2] == 'x..'):
                        c+=1
                    
                if ((v[0][i] == 'x' and v[0][i+2] =='x' and v[0][i+1] == '.') and (v[1][i:i+3] == '...')):
                    c+=1
                
                
                    
                    
                    
        for i in range(n-2):
            if (v[1][i] == 'x'):
                if i >0:
                    if (v[0][i-1:i+2] == '..x') or (v[0][i-1:i+2] == 'x..'):
                        c+=1
                    
                if ((v[1][i] == 'x' and v[1][i+2] =='x' and v[1][i+1] == '.') and (v[0][i:i+3] == '...')):
                    c+=1
                
        
            
            
        print(c)
            