for i  in range(int(input())):
    n = int(input())
    ans = sum(list(map(int,input().split())))
    
    if(int(ans**(1/2))**2 == ans):
        print("YES")
    else:
        print("NO")