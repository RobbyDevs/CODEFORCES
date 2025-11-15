n = int(input())
m = int(input())

if n > m:

    if (n//m)%2 == 0:
        print("MARCEL")
    else:
        print('JOAOZAO')
        
elif n == m:
    print('JOAOZAO')

else:
    print('MARCEL')