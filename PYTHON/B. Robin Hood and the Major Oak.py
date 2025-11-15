from math import ceil

for w in range(int(input())):
    
    n,k = map(int,input().split())
    ni = c = s = 0
    
    if k == 1:
        if n % 2 == 0:
            print('YES')
        else:
            print('NO')
        
    else:
    
        ni = ceil((n -(n-k)))
        if ni == 2:
            print('NO')
        elif ni>2 and ni %2 == 0:
            print('YES')
        else:
            if n %2 != 0:
                print('YES')
            else:
                print('NO')

            #todos os imp que vem antes de n-k nao contam   