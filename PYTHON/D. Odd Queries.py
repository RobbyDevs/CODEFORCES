for w in range(int(input())):
    n,q = map(int,input().split())
    
    v = list(map(int,input().split()))
    
    par = im = 0
    
    for i in v:
        if i %2 == 0:
            par +=1
        else:
            im+=1
            
    
    for vez in range(q):
        impar = im
        l,r,k = map(int,input().split())
        
        for i in range(l-1,r):
            if v[i]%2 == 0:
                if k%2 !=0:
                    impar +=1
                
            else:
                if k%2 == 0:
                    impar -=1
        if impar %2 == 0:
            print('NO')
        else:
            print('YES')
        
        
        
"""
quantos impares ha de x a y (inc)
x a y
1 a 5

y-(x+1)
5-2 = 3
1 3 5

2 a 6

6-3 = 3



"""
        
