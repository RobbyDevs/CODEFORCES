for w in range(int(input())):
    
    n = int(input())
    
    v = list(reversed(input()))
    vn = [str(x) for x in range(n,0,-1)] 
    #print(vn)
    #print(v)
    
    vr = []
    while len(v) >0:
        
        for i in range(len(v)):
            if v[i] == '<':
                #print(vn)
                mini = vn[len(vn)-1]
                vr.append(mini)
                vn.remove(mini)
                v.pop(i)
                
                break
            else:
                #print(vn)
                maxi = vn[0]
                vr.append(maxi)
                vn.remove(maxi)
                v.pop(i)
                break
    vr.append(vn[0])
    
    va= ' '.join(list(reversed(vr)))
    print(va)