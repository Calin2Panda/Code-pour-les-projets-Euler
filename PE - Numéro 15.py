a = int(input('Combien de largeur fait la grille ? : '))
b = int(input('Combien de longueur fait la grille ? : '))

def facto(n):
    d = 1
    for i in range(1, n+1):
        d = d * i
    return d

n = facto(a+b)
print(n/(facto(a)*facto(b)))