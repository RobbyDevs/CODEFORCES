for w in range(int(input())):
    n = int(input())
    
    v = list(map(int,input().split()))
    
    s = [0,1,0,3,2,5]
    ind = 0
    jj = 0
    isclean = False
    while isclean == False:
        isclean = False
        for i in range(ind,n):
            for j in range(len(s)):
                if i in v:
                    s.remove(i)
                    ind = j
                    if j > jj:
                        jj = j
                    isclean = False
                    break
            else:
                isclean = True
        
    
            
    print(jj)