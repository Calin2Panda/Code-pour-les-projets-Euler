
def aaa(i):
    j = 0
    d = 0
    while i != 1:
        if i%2 == 0:
            i = i/2
        else:
            i = 3*i+1
        d += 1
    if d > j:
        j = d
    j += 1
    return j
l = [0]
for each in range(1, 1000001):
    l.append(aaa(each))
print(l.index(525))
print('le nombre de terme dans les opérations avant que les fonctions donnent 1 est égale à :', max(l))