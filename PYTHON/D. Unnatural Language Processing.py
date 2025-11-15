ct = int(input())  
          

for _ in range(ct):
    
    l = int(input())
    ss = input()
    
    v = 'ae'
    c = 'bcd'
    
    s = []
    sy = []
    p = ['.']
    a = 0
    brake = False
    fin = False
    sf = []
#   b a b a    >>    b a c e d b a b

    
    for i in range(0,l):
        
        if brake == True:
            sy.append(a)
            brake = False
       

        if len(sy) == 2:
            if  i < (l - 1):
                
                if ss[i+1] in c:
                    sy.append(ss[i])
                    
                elif ss[i+1] in v:
                    a = ss[i]
                    brake = True
                    
            elif i == (l - 1):
                sy.append(ss[i])
                fin = True  
        
        else:
            sy.append(ss[i])
            if i == l -1:
                fin = True
        
        if len(sy) == 3 or (len(sy) == 2):
            
            
            s.append(sy)
            if fin == False:
                s.append(p)
            sy = []
        
    print(s)
    

#preciso encontrar uma forma de cortar a silaba em len 2 quando o valor ss[i+1] for par.
    