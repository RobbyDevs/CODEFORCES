for w in range(int(input())):
    
    n = int(input())
    
    v = list(map(int,input().split()))
    
    soma = sum(v)
    
    for i in v:
        
        if ((soma-i) %2 ==0 and i%2 == 0) or ((soma-i)%2 != 0 and i % 2 != 0):
            print('YES')
            break
    else:
        print('NO')