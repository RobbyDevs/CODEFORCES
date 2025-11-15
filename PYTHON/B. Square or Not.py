for w in range(int(input())):
    n = int(input())
    
    v = input()
        
    if n < 4:
        print('NO')
    else:
        if n == 4:
            print('YES')
        else:
            s = v.count('0')
            if (int(n**(1/2))**2) == n:
                if (int(s**(1/2))**2) == s and s>0:
                    print('YES')
                else:
                    print('NO')
            else:
                print('NO')