for i in range(int(input())):

    s = input()
    a = b = 0
    
    for j in s:
        if j == 'A':
            a+=1
        else:
            b+=1
        
    if a>b:
        print('A')
    else:
        print('B')