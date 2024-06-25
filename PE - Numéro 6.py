def caca(a):
    return a**2
b = 0
c = 0
for i in range(1, 101):
    b += caca(i)
    c += i
c = c**2
print(c-b)
