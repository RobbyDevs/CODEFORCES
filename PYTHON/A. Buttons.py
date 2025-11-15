for w in range(int(input())):
    
    a,b,c = map(int,input().split())
    
    fi = a+(c//2)
    fs = b+(c//2)
    
    if c%2 !=0:
        fi +=1
        
    
    if fi > fs:
        print('First')
    else:
        print('Second')