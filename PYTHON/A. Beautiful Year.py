v = int(input())

while True:
    v+=1
    if len(list(set(str(v)))) == len([str(x)for x in str(v)]):
        print(v)
        break

