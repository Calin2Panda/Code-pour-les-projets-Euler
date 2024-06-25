a = 2
b = [1,2]
while b[len(b)-1] < 4000000 :
    b.append(b[len(b)-1]+b[len(b)-2])
    if b[len(b)-1] % 2 == 0:
        a += b[len(b)-1]
        print(a)
        print(b)
print(a)
print(b)