ct = int(input())

for i in range(ct):
    a,b = map(int,input().split())

    if a>=b:
        print(a)

    elif (a)*2 <= b:
        print(0)
    
    elif (a)*2>b:
        print(a-(b-a))