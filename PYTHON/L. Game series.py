a1,p1 = map(int,input().split())
a2,p2 = map(int,input().split())

if a1+a2 > p1+p2:
    print("A")
elif a1+a2 < p1+p2:
    print('P')
else:
    print('D')