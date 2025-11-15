for w in range(int(input())):
    
    v = [str(x) for x in input()]
    
    ant = ''
    
    for i in range(len(v)-1):
        if v[i] == v[i+1]:
            if v[i] == 'a':
                v.insert(i+1,'z')
                break
            else:
                v.insert(i+1,'a')
                break
                
    else:
     
        if v[-1] == 'a':
            print(*v,'b',sep='')
            continue
        
        else:
            print(*v,'a',sep='')
            continue
        
    print(*v,sep='')
            
    