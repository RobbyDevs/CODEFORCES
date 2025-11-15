for i in range(int(input())):
    
    n,m,a,b = map(int,input().split())
    nn = n
    mm = m
    cn = cm = 0
    if n%2 != 0:
        if m%2 != 0:
            cn+=1
            if a == ((n//2)+1) and b == (m//2)+1:
                cn+=1
        else:
            if a == ((n//2)+1):
                cn+=1
    else:
        if m%2 !=0:
            if b == ((m//2)+1):
                cm+=1
        else:
            if (a%2!=0 or b %2!=0) and (a>2 or b>2):
                cm +=1

            
    cont  = 1
    c = 0
    while mm>1:
        mm=mm//2
        cm+=1
        if mm >3 and mm%2 !=0 and cont == 0:
             if c == 0:
                cont =1
                c = 1
                cn+=1
                
                
    while nn>1:
        nn = nn//2
        cn+=1
        
        if nn >3 and nn%2 !=0 and cont == 0: 
            
            if c == 0:
                cont =1
                c = 1
                cn+=1
            

        
    print(cm+cn)
        
    