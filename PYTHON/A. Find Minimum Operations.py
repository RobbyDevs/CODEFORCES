nc = int(input())
for i in range(0,nc):
    n,k = map(int,input().split())
    nb = n
    npk=op=0

    while True:
        if k==1:
            op=n
            break
        
        if nb == 0:
            break
        else:
            for i in range(0,10):
                if k**i > nb:
                    nb=nb-(k**(i-1))
                    op+=1

                    break
    print(op)