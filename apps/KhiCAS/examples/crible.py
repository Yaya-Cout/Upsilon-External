def crible(n):
    # local tab,prem,p
    tab=list(range(n+1))
    tab[0]=0
    tab[1]=0
    p=2
    while p*p<=n :        
        j=p*p
        while j<=n :
            tab[j]=0
            j=j+p
        p=p+1
        while p*p<=n and tab[p]==0 :
            p=p+1
    prem=[]
    for j in range(2,n+1):
        if tab[j]!=0 :
            prem.append(j)
    return(prem)

print(crible(100))
