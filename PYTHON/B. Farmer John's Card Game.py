for w in range(int(input())):
    
    n,m = map(int,input().split())
    
    vm = []
    dic = {}
    
    for i in range(n):
        vm.append(sorted(list(map(int,input().split()))))
        
    for i in range(len(vm)):
        dic[i+1] = vm[i]

    print(dic)
    
    dic = dict(sorted(dic.items(),key= lambda x: x[0]))

    print(dic)