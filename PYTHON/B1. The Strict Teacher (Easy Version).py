for w in range(int(input())):
    
    n,m,q = map(int,input().split())
    
    p1,p2 = map(int,input().split())
    
    d = int(input())
    
    dif1 = d-p1
    dif2 = d-p2
    
    if (dif1 <0  and dif2 < 0) or (dif1 > 0 and dif2>0):
        s = 0
        if p1 > d:
            
            s = d-1
        else:
            s = n-d
            
            
        
        print((min(abs(n-(abs(dif1))),abs(n-(abs(dif2))))-1) + (s))
    else:
        
        if (abs(d-p1) == 1) or (abs(d-p2) == 1):
            print(1)
            
        else:
            if abs((abs(p1-d) - abs(p2-d))) <=1:
                print(min((abs(p1-d)),abs(p2-d)))
                
            else:
                d = max(dif1,dif2)- min(dif1,dif2)
                
                print(min(abs(p1-d),abs(p2-d))-1)
                
                