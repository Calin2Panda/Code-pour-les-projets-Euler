c = 0
o, u = 0, 0
for i in range(999, 99, -1):
    for j in range(999 , 99, -1):
        a = i*j
        k = str(a)
        k1 = list(k)
        k2 = list(reversed(k))
        if k1 == k2:
            if c < a:
                c = a
                o = i
                u = j
                print(c,o,u)

