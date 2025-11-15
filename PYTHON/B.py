for w in range(int(input())):
    
    n,k = map(int,input().split())
    nn = n
    nn = nn-(k-1)
    if nn %2 == 0:
        n = n-((2*k)-1)
        if n %2==0:
            print('YES')
            print('2'*(k-1),n,sep='')
        else:
            print('NO')
        
    else:
        print('YES')
        print("1"*(k-1),nn,sep='')