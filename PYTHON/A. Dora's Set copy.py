for w in range(int(input())):
    
    l,r = map(int,input().split())
    
    v = [x for x in range(l,r+1)]
    #print(len(v))
    
    #print(v)
    #print("<VVVVV")
    if len(v)<3:
        print(0)
    else:
    
        ind = 0
        c = 0
        for i in range(len(v)):
            if v[i]%2 !=0:
                ind +=1
                if ind == 2:
                    c+=1
                    #print(v[i])
                    ind = 0
        print(c)