for w in range(int(input())):
    
    va = [0,0,0]
    n = int(input())
    
    v = list(map(int,input().split()))
    
    s = n//3
    c = 0
    for i in v:
        if i %3 == 0:
            va[0]+=1
        elif i%3 == 1:
            va[1]+=1
        else:
            va[2] +=1
            
            
    if va[0] == va[1] == va[2]:
        print(0)
        
    else:
        #print(va)
        while True:
            
            for i in range(3):
                
                if va[i] < s:
                    
                    if va.index(max(va)) - i == -1:
                        c+=1
                    elif va.index(max(va)) - i == -2:
                        c+=2
                    elif va.index(max(va)) - i == 1:
                        c+=2
                    elif va.index(max(va)) - i == 2:
                        c+=1
                    va[va.index(max(va))] -=1
                    va[i] +=1
                    
                
                    
                    break         
                    
            else:
                break
        
        #print(va)
        print(c)

