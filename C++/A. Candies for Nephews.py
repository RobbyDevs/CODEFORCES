for w in range(int(input())):
    n = int(input())
    ans = n%3
    
    if ans ==0:
        print(ans)
    else:
        ans = 3-ans
        print(ans)