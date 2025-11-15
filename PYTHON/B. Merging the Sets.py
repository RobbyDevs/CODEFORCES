import sys

input = sys.stdin.readline

def solve():
    n,m = map(int,input().split())
    grafo = [[] for x in range(m+10)]
    #print(grafo)
    vl = []
    for i in range(n):
        vl .append(list(map(int,input()[1:].split())))
        
    #print(*vl,sep='\n')
        
        
    
    for i in range(n):
        for j in range(len(vl[i])):
            grafo[vl[i][j]].append(i+1)
            
    
    vf = [0]*(m+10)
    
    
    for i in range(1,m+1):
        if len(grafo[i]) == 0:
            print("NO")
            return
    
    for i in grafo:
        if len(i)>0:
            vf[len(i)]+=1
            
    soma = sum(vf[2:])
    #print(vf)
    #print(soma)
    
    if soma >= vf[1]:
        print("YES")
    else:
        print("NO")
    
for w in range(int(input())):
    solve()