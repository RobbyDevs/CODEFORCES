for i in range(int(input())):
    a,b,c = map(int,input().split())
    
    c = c-(b-a)
    a = a+(b-a)
    
    #print('>>',a,b,c)
    if a == b and b == c:
        print('YES')
    else:
        if (c>a and c>b) and (c-a == c-b) and (c-a)%3 == 0:
            print('YES')
        else:
            print('NO')

    
    
    #print('>>',a,b,c)