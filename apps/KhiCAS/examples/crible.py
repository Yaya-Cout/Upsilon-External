def crible(n):
    # local tab,prem,p
    tab=list(range(n+1))
    tab[0]=0
    tab[1]=0
    p=2
    while p**2 <= n:    
        j = p**2
        while j<=n :
            tab[j]=0
            j=j+p
        p += 1
        while p**2 <= n and tab[p] == 0:
            p += 1
    return [j for j in range(2,n+1) if tab[j]!=0]

print(crible(100))
