w = int(input())

for w in range(w):
    a,b = map(int,input().split())
    vm = [a,b]
    m = min(vm)
    
    
    while True:        
        if m % a == m % b:
            print(m)
            break
        else:
            m+=1