c = 0
n = int(input())
v = list(map(int,input().split()))
    
c = ((sum(v))/(n*100))*100

print(f'{c:.4f}')