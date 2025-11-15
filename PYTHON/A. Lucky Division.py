n = int(input())

for i in range(4,n+1):
    for j in str(i):
        if j not in '47':
            break
    else:
        if n % i==0:
            print('YES')
            break
else:
    print('NO')