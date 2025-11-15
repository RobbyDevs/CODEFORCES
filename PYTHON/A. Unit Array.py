for w in range(int(input())):
    
    n = int(input())
    
    v = list(map(int,input().split()))
    
    nn = 0
    np = 0
    for i in v:
        if i ==1:
            np+=1
            
        else:
            nn+=1
    
    #print('vvvvvvvvvvv')
    if nn == np:    #sum == 0
    
        if nn == 0 or nn %2 ==0:
            print(0)
        else:
            print(1)
            
    elif np > nn:
        if nn == 0 or nn % 2 == 0:
            print(0)
        else:
            print(1)
    else:
        if np == 0:
            if nn == 2:
                print(2)
                
            elif nn%2 == 0:
                print(nn//2)
            else:
                if nn == 3:
                    print(3) 
                else:   
                    print((nn//2)+1)
            

        else:
            dif = nn-np
            
            if dif %2 == 0:
                print(dif//2)
                
            else:
                c = 0
                
                
                print((dif//2)+1)