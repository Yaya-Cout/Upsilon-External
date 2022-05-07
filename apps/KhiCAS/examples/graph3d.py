# https://my.numworks.com/python/schraf/graph3d
from math import *
from kandinsky import *

def f0(x,y): return 5*x*sin(5*y)
def f1(x,y): return 10*sin(4*x)*y
def f2(x,y): return 90*cos(x*x+y*y)*exp(-(x*x+y*y)/5)
def f3(x,y): return -400/exp(x*x+y*y)
def f4(x,y): return 80*cos(2*y)/(x*x+y*y+0.001)-50
def f5(x,y): return 5*sin(x*(y+4))*y
def f6(x,y): return -y*y/(x*x+0.001)


def eff():
  fill_rect(0,0,320,240,(0,)*3)
      
def go(f,xmax=4,ymax=4):
  eff()
  h,v = 160,80
  for i in range(-h,h,1):
    m,n = 0,220
    for j in range(v,-v,-1):
      x = -xmax*i/h+xmax*j/v
      y = ymax*i/h+ymax*j/v
      #if abs(x) <= xmax and abs(y) <= ymax:
      if (x / xmax)**2 + (y / ymax)**2 <= 1:
        z = 110+j-f(x,y)
        if z >= m or z <= n:
          m = max(z,m)
          # lumiere ou ombre
          c = (255,)*3 if z < n else (68,)*3
          n = min(z,n)
          set_pixel(i+160,int(z),c)
