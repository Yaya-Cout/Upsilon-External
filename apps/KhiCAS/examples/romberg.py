from math import *
def Trapezes(f,a,b,N):
    # local h,j,s
    h=float(b-a)/N
    s=(f(a)+f(b))/2.0
    for j in range(1,N):
        s += f(a+j*h)
    return h*s

def Romberg(f,a,b,eps):
    twopow=1
    T=[Trapezes(f,a,b,1)]
    for j in range(1,10):
        twopow *= 2
        newT=[Trapezes(f,a,b,twopow)]
        fourpow=1
        for k in range(j):
            fourpow *= 4
            newT.append((fourpow*newT[k]-T[k])/(fourpow-1))
        if abs(T[-1]-newT[-1])<eps:
            return newT[-1]
        T=newT
    return "Pas de convergence"

print(Romberg(lambda x:exp(-x**2),0,2,1e-10))
