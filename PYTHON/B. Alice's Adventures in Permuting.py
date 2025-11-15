def solve():
    n, b, c = map(int, input().split())
    
    if b == 0:
        if n-c>2: print(-1)
        else: 
            if c < n: print(n-1)
            else: print(n)
        return
    
    k = (n - c) // b
    if k * b + c <= n-1: k+=1
    s = min(n, n-k)
    print(s)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()