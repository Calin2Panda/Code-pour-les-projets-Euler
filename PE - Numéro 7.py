a = [2]
i = 3
b = True
while len(a) < 1000 :
    for j in range(len(a)):
        if b == True:
            if i % a[j] == 0 and b == True:
                b = False
            elif i % a[j] != 0 and j == len(a)-1:
                a.append(i)
    i += 2
    b = True
print(i)
print(a)