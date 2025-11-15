for w in range(int(input())):
    
    n,k,pb,ps = map(int,input().split())
    
    vp = list(map(int,input().split()))
    va = list(map(int,input().split()))
    
    cb = va[vp[pb-1]-1]
    cs = va[vp[ps-1]-1]
    
    #print(cb)
    #print(cs)

    if k == 1:
        if cb>cs:
            print('Bodya')
        elif cb<cs:
            
            print('Sasha')
        else:
            print('Draw')
    else:
        if cb == cs:
            print('Draw')
        else:   
            mai = max(va)
            
            nmai = va.count(mai)
            
            if nmai >1:
                print('Draw')
            
            else:
                if cs == mai:
                    print('Bodya')
                elif cb == mai:
                    print('Sasha')
                else:
                    if cb>cs:
                        print('Bodya')
                        
                    elif cs>cb:
                        print('Sasha')
                    else:
                        print('Draw')
    print('^^^^')