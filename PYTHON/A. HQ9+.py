s = input()

v = 'HQ9'
for i in s:
    if i in v:
        print('YES')
        break
else:
    print('NO')