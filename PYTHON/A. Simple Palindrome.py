s = 'aeiou'

for w in range(int(input())):
    n = int(input())
    v = []
    if n <= len(s):
        for i in range(n):
            v.append(s[i])
            
        print(*v,sep='')
    else:
        v = []
        dif = n - len(s)
        
        res = n%len(s)
        div = n//len(s)
        
        #print(res,div)
        for i in s:
            for j in range(div):
                v.append(i)
                
            if res > 0:
                v.append(i)
                res -=1
                
        print(*v,sep='')