    ct = int(input())

    for w in range(ct):
        n,k = map(int,input().split())
        v = list(map(int,input().split()))
        vm = []
        kk = 0
        
        if max(v)==k:
            print('0')
        
        elif (max(v) == min(v)) and sum(v)<k:
            print(abs(sum(v)-k))
            
        
        else:
            for i in range(n):
                if v[i] == max(v[i:]):
                    vm.append(v[i])
                    
            if sum(vm)<= k:
                
                print(abs(k-sum(vm)))
            
            else:
                for j in range(len(vm)):
                    if kk + vm[j] > k:
                        print(abs(sum(vm[0:j])-k))
                    elif kk + vm[j]<k:
                        kk += vm[j]
                    else:
                        print(0)
                        break