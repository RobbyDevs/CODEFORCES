for w in range(int(input())):
    
    n,m = map(int,input().split())
    
    v = [str(x) for x in input()]
    v.sort()

    dic = {"A":0,"B":0,"C":0,"D":0,"E":0,"F":0,"G":0}
    
    for i in v:
        try:
            dic[i]+=1
            
        except KeyError:
            dic[i]=1
            
    s = 0
    for i in dic.values():
        if i<m:
            s+= i-m
    print(abs(s))