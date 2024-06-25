a = int(input('La puissance que l\'on va appliquer sur 2 ? : '))
b = str(2**a)
c = list(b)
d = 0
for i in range(len(c)):
    d += int(c[i])
print(d)