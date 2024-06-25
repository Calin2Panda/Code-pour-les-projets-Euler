from num2words import num2words

d = 0
for j in range(1, 1001):
    a = num2words(j)
    b = list(a)
    c = 0
    for i in range(len(b)):
        if b[i] == ' ' or b[i] == '-':
            c += 1
        
    d += len(b)-c

print(d)