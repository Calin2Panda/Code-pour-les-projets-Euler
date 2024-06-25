x, y, z = 1 , 1, 1
p, q = 2, 1

def px(p, q):
    return (p**2)-(q**2)

def py(p,q):
    return 2*p*q

def pz(p,q):
    return (p**2)+(q**2)

while x + y + z != 1000:
    x = px(p,q)
    y = py(p,q)
    z = pz(p,q)
    if p < 1000:
        p += 1
    else:
        q += 1
        p = q +1
    print(x+y+z)

print(x,y,z, x+y+z)