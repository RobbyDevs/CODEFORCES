for w in range(int(input())):
    n,k,x = map(int,input().split())
    
    
    if x == 1:
        if k == 1:
            print('NO')
            
        elif k == 2:
            if n % 2 == 0:
                print('YES')
                print(n//2)
                print('2 '*(n//2))
                
            else:
                print('NO')
        elif k >= 3:
            
            if n %2 == 0:
                print('YES')
                print(n//2)
                print('2 '*(n//2))
            else:
                
                if n % 3 == 0:
                    print('YES')
                    print(n//3)
                    print('3 '*(n//3))
                else:
                    print('YES')
                    print(1+((n-3)//2))
                    print(3,'2 '*((n-3)//2))
                               
                                    
            
        
    else:
        print('YES')
        print(n)
        print('1 '*n)