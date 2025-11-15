
def calcularAtaque(x,y, a,b):
    
    if a == b:
        ataques =[[x-a,y+b],[x-a,y-b],[x+a,y-b],[x+a,y+b]]
    else:
        
        ataques=[[x-a,y+b],[x-b,y+a],[x-a,y-b],[x-b,y-a],[x+a,y-b],[x+b,y-a],[x+a,y+b],[x+b,y+a]]
        
    return ataques

def solve():
    a,b = map(int,input().split())
    xk,yk = map(int,input().split())
    xq,yq = map(int,input().split())
    
    king = calcularAtaque(xk,yk,a,b)
    queen = calcularAtaque(xq,yq,a,b)
    
    ans = 0
    for i in king:
        if i in queen:
            ans+=1
                
    print(ans)
    #print("^^^^^^")
    #print(king)
    #print(queen)
    
for w in range(int(input())):
    solve()