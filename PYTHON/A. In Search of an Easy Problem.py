n = int(input())

v = list(map(int,input().split()))

if sum(v) > 0:
    print('HARD')
    
else:
    print('EASY')