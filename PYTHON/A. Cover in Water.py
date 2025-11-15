ct = int(input())

for _ in range(ct):
    n = int(input())
    
    s = input().split('#')
    
    
    
    nl =0
    for i in range(0,len(s)):
        if len(s[i]) > nl:
            nl = len(s[i])
            
    if nl >= 3:
        print(2)
    elif nl == 0:
        print(0)
        
    else:
        st = [str(x) for x in (''.join(s)) if x =="."]
        print(len(st))