#maior seq com *01*
def maiord(v):
    seq= []
    ant = v[0]
    t = ant
    for i in range(1,len(v)):
        if v[i]>=ant:
            t+=v[i]
            ant = v[i]
        else:
            seq.append(t)
            ant = v[i]
            t = ant
    seq.append(t)
    
    
    #print(seq)
    
    lmai = 0
    ms = ''
    ind = 0
    for i in range(len(seq)):
        if len(seq[i])>1:
            if seq[i][0]!=seq[i][-1]:
                if len(seq[i])>lmai:
                    lmai = len(seq[i])
                    ms = seq[i]
                    ind = i
    seq.pop(ind)
    
    return [ms,''.join(seq)]
    
    
for w in range(int(input())):
    
    v = input()
    ma01, nv = (maiord(v))
    
    #print(ma01,nv)
    #print('vvvvvvvvv')

    if nv == '':
        print(1)
    else:
        ant = nv[0]
        grupos = []
        t = ant
        for i in range(1,len(nv)):
            if nv[i]== ant:
                t+=nv[i]
            else:
                grupos.append(t)
                t = nv[i]
                ant = t
        grupos.append(t)
        
        print(1+len(grupos))
#grupos de 1 e 0
