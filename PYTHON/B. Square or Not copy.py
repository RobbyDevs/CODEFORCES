for w in range(int(input())):
    n = int(input())
    
    v = input()
        
    if n < 4 or (int((n**(1/2)))**2) != n:
        print('No')
    else:
        #nn = n**(1/2)
        if v == '1111':
            print('YES')
        else:
            j = n-1
            for i in range(n):
                if