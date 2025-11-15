for w in range(int(input())):
    
    n = int(input())
    
    
    v = list(map(int,input().split()))
    
    co = 0 
    mai = 0
    for i in range(n):
        if v[i] == 0:
            co +=1
            if co > mai:
                mai = co
        else:
            co = 0
    #print('>>')    
    print(mai)