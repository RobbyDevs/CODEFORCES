import sys
input  = sys.stdin.readline

def euc (x1,x2,y1,y2):
    val = (((x1-x2)**2)+((y1-y2)**2))**(0.5)
    return val

def solve():
    n = int(input())
    
    px,py,qx,qy = map(int,input().split())
    
    vn = list(map(int,input().split()))
    
    somavn = sum(vn)
    disPQ = euc(px,py,qx,qy)
    if disPQ > somavn:
        print("NO")
    elif disPQ == somavn:
        print("YES")

    else:
        print("dis P-Q",disPQ)
        
for w in range(int(input())):
    solve()
