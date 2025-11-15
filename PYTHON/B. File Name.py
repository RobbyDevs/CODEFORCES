n = int(input())

s = input()

if 'xxx' not in s:
    print(0)

else:
    sl = [str(x) for x in s]
    c = False
    r = 0
    while c != True:

        co = 0
        c = True
        for i in range(len(sl)):
            if sl[i] == 'x':
                co+=1
            else:
                co = 0
                
            if co == 3:
                sl.pop(i)
                co = 0
                c = False
                r +=1
                break

    print(r)