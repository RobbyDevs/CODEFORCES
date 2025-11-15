w = int(input())
c = 0

if w > 2:
    
    if ((w/2) % 2 == 0):
        print('YES')
        c = 1

    else:
        for i in range(2,w+1,2):
            if (w - i) %2 == 0:
                print('YES')
                print(w-i,i)
                c = 1
                break
if c == 0:
    print('NO')