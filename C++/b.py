for w in range(int(input())):
    n = int(input())
    a,b = input().split()
    
    va = [x for x in a]
    vb = [x for x in b]
    
    va.sort()
    vb.sort()
    
    if va == vb:
        print('YES')
    else:
        print("NO")