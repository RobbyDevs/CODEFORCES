for w in range(int(input())):
    
    l,r = map(int,input().split())
    c = 2*(r-l)
    
    b = a = 1
    d = 4*a*c   
    x1 = (-b + (b**(1/2)**2)+d)/2
    x2 = (-b - (b**(1/2)**2) + d)/2
   
    print(int(max(x1,x2)))