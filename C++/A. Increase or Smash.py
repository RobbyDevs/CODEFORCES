for w in range(int(input())):
    
    n = int(input())
    
    v = list(map(int,input().split()))
    v = set(v)
    print((len(v)*2)-1)