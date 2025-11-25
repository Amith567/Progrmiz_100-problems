import math

def discriminant(a,b,c):
    d=(b**2)-(4*a*c)
    return d

def tworealroot(d,a,b):
    d=(d)**0.5
    root1=(-b+d)/(2*a)
    root2=(-b-d)/(2*a)
    return root1,root2
def onerealroot(a,b):
    root=(-b)/(2*a)
    return root

print("enter the coeficieants of a, b & c : ")
a=int(input())
b=int(input())
c=int(input())

d=discriminant(a,b,c)
if d>0:
    root1,root2=tworealroot(d,a,b)
    print(f"first root {root1}")
    print(f"second root {root2}")
elif d==0:
    root=onerealroot(a,b)
    print(f"root {root}")
else:
    print("no root for this problem.")