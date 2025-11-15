for w in range(int(input())):
    
    n,m = map(int,input().split())
    
    vm = []
    dic = []
    
    for i in range(n):
        vm.append(sorted(list(map(int,input().split()))))
        
    for i in range(len(vm)):
        dic.append([i+1,vm[i]])

    #print(dic)
    
    dic.sort(key= lambda x: (x[1]))
    
    #print(dic)
    #print('vvvvv')
    if m == 1:
        for i in range(len(dic)):
            print(dic[i][0],end=' ')
        print()
            
            
    else:
        con = 0
        for i in range(len(dic)):
            for j in range(len(dic[i])-1):
                if abs(dic[i][1][j+1]-dic[i][1][j]) != n:
                    con = 1
                    break   
            if con == 1:
                break
        if con == 1:
            print(-1)
        else:
            for i in range(len(dic)):
                print(dic[i][0],end=' ')
            print()
            
                        