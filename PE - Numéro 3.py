a = 600851475143
b = [2]
c = 0
while a > 1:
    if a % b[len(b)-1] == 0:
        a = a / b[len(b)-1]
        c = b[len(b)-1]
    else:
        b.append(b[len(b)-1]+1)
print(c)