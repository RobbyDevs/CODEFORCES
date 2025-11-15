for w in range(int(input())):
    
    v = [int(x) for x  in input()]
    
    if sum(v[0:3]) == sum(v[3:]):
        print("YES")
    else:
        print("NO")