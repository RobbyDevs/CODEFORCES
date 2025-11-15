for w in range(int(input())):
    
    m = []
    
    n = int(input())
    
    #tr
    sa = s =0
    va = []
    for i in range(n):
        v = input()
        
        cou = v.count('1')
        if cou >0: va.append(cou)
        

    #print(va)
    

    
    va.sort()
    
    for i in range(len(va)-1):
        if int(va[i+1]) - int(va[i]) != 0:
            print('TRIANGLE')
            break
    else:
        print('SQUARE')