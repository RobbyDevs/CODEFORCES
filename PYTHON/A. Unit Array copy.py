
for w in range(int(input())):
    n = int(input())
    
    v = list(map(int,input().split()))
    nn = np =0
    
    for i in v:
        if i == 1: np+=1
        else: nn+=1
    
    
    if np>=nn:
        if nn%2 == 0:
            print(0)
        else:
            print(1)
    else:
        c = 0
        while True:
            if np>=nn and nn%2==0:
                break
            c+=1
            np+=1
            nn-=1

        print(c)


