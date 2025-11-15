from math import gcd
for w in range(int(input())):
    
    l,r = map(int,input().split())
    
    v = [x for x in range(l,r+1)]
    
    #print(v)
    
    #print(len(v))
    n = len(v)
    
    cc = 0
    while len(v) > 2:
        
        #print(v)
        
        a = v[0]
        v.pop(0)
        ind = 0
        while (v[0]%2 == 0 and v[ind]%2 == 0):
            ind+=1
            
        b = v[ind]
        v.pop(ind)
        #print(v)
        
        for i in range(len(v)):
            c = v[i]
            if gcd(a,c) == 1 and gcd(b,c) == 1:
                v.pop(i)
                
                #print('>>',a,b,c)
                cc+=1
                break
        else:
            break
    
    print('>>>>>',cc)
    
#print(v)