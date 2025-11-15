for w in range(int(input())):
    n = int(input())
    
    va = list(map(int,input().split()))
    vb = list(map(int,input().split()))
    
    
    m = int(input())
    
    vd = list(map(int,input().split()))
    
    vaa = list(va)
    vc = []
    n404 = []
    
    for i in range(m):
        try:
            if len(n404) == 0:
                vc.append(vb.index(vd[i])+1)
            else:
                a = vb.index(vd[i])+1
                for i in range(len(n404)+1):
                    vc.append(a)
                n404 = []
                    
        except ValueError:
            if i<m-1:
                n404.append(vd[i])
            else:
                for i in range(len(n404)+1):
                    vc.append(vd[-1])
                
    #print(vaa)
    #print(vb)
    #print(vc)
    for i in range(m):
        vaa[vc[i]-1] = vd[i]
        
    
    #print(vaa)
    
    if vb == vaa:
        print('YES')
    else:
        print('NO')
        
    
    
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



