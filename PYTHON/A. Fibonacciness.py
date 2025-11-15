for w in range(int(input())):
    a,b,d,e = map(int,input().split())
    
    
    ans = 0
    for c in range(-100,101):
        s = 0
        
        if a+b == c:
            s+=1
        if b+c == d:
            s+=1
        if c+d == e:
            s+=1
        #print(s)
        if s > ans:
            ans = s 
            #print('>>>>>')
    print(ans)
        