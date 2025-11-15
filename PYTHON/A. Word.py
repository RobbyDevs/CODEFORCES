v = input()

M = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
m = 'abcdefghijklmnopqrstuvwxyz'

mai = minu = 0
for i in v:
    if i in M:
        mai +=1
    else:
        minu +=1
        
if mai>minu:
    print(v.upper())

else:
    print(v.lower())