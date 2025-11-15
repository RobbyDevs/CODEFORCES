import sys

input = sys.stdin.readline

def solve():
    
    dic = {}
    n,m = map(int,input().split())
    
    v = input()
    
    #print(v)
    pont = 1
    for i in list(map(int,input().split())):
        dic[i] = 1
        
    
    for i in range(n):
        if i == 0 and v[i] == 'B':
            for j in range(2,int(10e9)):
                if j not in dic:
                    pont = j
                    dic[j] = 1
                    break
                
        if v[i] == "B":
            for j in range(2,n):
                if j not in dic:
                    pont = j
                    dic[j] = 1
                    break
        
        
        else: 
            pont+=1
            if pont not in dic:
                dic[pont] = 1
                
        #print(dic)
            
            
        
    print(*sorted(dic.keys()),sep=" ")
    ans = m
    
    
    
    
    
for w in range(int(input())):
    solve()