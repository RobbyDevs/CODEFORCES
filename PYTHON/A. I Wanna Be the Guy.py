n = int(input())
va = list(map(int,input()[1:].split()))
vb = list(map(int,input()[1:].split()))

va.extend(vb)

vm = list(set(va))

if len(vm) <n:
    print("Oh, my keyboard!")
else:
    print("I become the guy.")