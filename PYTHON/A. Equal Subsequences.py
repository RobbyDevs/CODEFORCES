for w in range(int(input())):
    n,k = map(int,input().split())
    
    
    if n == 1:
        print(1)
    elif n == 2:
        print(11)
    elif n == 3:
        print(111)
    else:
        if k == n:
            print("1"*k)
        else:
            c1 = k-2
            print(10,end='')
            for i in range(n-4):
                if c1>0:
                    print(1,end='')
                    c1-=1
                else:
                    print(0,end='')
            print(10)
        
    
        
"""

111

1010


"""