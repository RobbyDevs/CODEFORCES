c = 0
for w in range(int(input())):
    v = list(map(int,input().split()))
    if sum(v) >= 2:
        c +=1

print(c)