for w in range(int(input())):
    
    a,b = input().split()
    a = [str(x) for x in a]
    b = [str(x) for x in b]
    a[0],b[0] = b[0],a[0]
    
    print(''.join(a),''.join(b))