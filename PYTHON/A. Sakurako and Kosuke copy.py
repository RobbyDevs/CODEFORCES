nc = int(input())

for i in range(nc):


    n = int(input())
    p= 0
    v= False
    s=0
    j = 1
    while True:
        if v == False:
            s = ((j*2)-1)*(-1)
        else:
            s = (j*2)-1
        p = p + s
        if p > n or p < (n*-1):
            break
        v = not v
        j+=1

    if v == False:
        print('Sakurako')
    else:
        print('Kosuke')
        
