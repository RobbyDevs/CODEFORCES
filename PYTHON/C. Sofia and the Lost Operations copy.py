for w in range(int(input())):
    n = int(input())
    
    va = list(map(int,input().split()))
    vb = list(map(int,input().split()))
    
    
    m = int(input())
    
    vd = list(map(int,input().split()))
    dic = {}
    for i in range(n):
        dic[vb[i]] = i+1
            
    vc = []
    faltam = []
    for i in range(m):
        if vd[i] in dic:
            if len(faltam) == 0:
                vc.append(dic[vd[i]])
            else:
                for j in range(len(faltam)+1):
                    vc.append(dic[vd[i]])
                faltam = []
        
        else:
            faltam.append(vd[i])
            if i == m-1:
                for i in range(len(faltam)+1):
                    vc.append(n-1)
           
    """print(va)
    print(vc)
    print(vd)
    print(vb)"""
         
    for i in range(m):
        #print(vc[i-1])
        va[vc[i]-1] = vd[i]
        
    if va == vb:
        print('YES')
    else:
        print("NO")
                
            
    
            
    
    
"""

1 2 1

1 3 2

4

- - - -
1 3 1 2
-----------

1 2 3 5

2 1 3 5

2

1 3
2 3 -> array d n possui 1 para mudar a[2]

-----------

7 6 1 10 10
3 6 1 11 11

3

- 7 10
4 3 11 -> 11 eh usado 2x, mas so ha um em d;
       -> 4 nao foi usado.

-------------


3 1 7 8
2 2 7 10

5
4  1 1 2 - 
10 3 2 2 1  -> 3 n eh usado
            -> 1 n eh usado

-----------

5
5 7  1 7 9
4 10 1 2 9
8

3 3 5 4 4 4 2  1 
1 1 9 8 7 2 10 4




"""



