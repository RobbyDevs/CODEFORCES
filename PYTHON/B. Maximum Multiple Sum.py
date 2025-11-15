for w in range(int(input())):
    
    n = int(input())
    
    sp = si = 0
    
    for i in range(2,n+1):
        if i %2 ==0:
            sp+=1
        if i%3 == 0:
            si +=1
            
    if sp>si:
        print(2)
    else:
        print(3)