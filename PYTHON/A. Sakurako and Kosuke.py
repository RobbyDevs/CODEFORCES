nc = int(input())

for i in range(nc):


    n = int(input())
    p= 0
    v= False
    s=0
    while True:
        if v == False:
            s = (-p*2)-1
        else:
            s = (p*2)-1
        p = p + s
        print(p)
        if p > n or p < (n*-1):
            break
        v = not v

    if v == False:
        print('Sakurako')
    else:
        print('Kosuke')
        
