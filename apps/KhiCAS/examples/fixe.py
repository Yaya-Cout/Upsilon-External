def fixe(f,u0,N,eps):
  # local j,u1
  u0=u0*1.0 
  for j in range(N):
    u1=f(u0)
    if abs(u1-u0)<eps*abs(u0):
      return u1,j
    u0=u1
  return "Pas de convergence"

from math import *
f=lambda x:cos(x)
print(fixe(f,0.0,100,1e-8))
