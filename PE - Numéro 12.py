from sympy import divisors

def a():
    a = 1
    b = []
    c = True
    d = 1
    while len(b) < 6:
        b = []
        for i in range(1,a+1):
            if a % i == 0 and c == True:
                b.append(i)
                c = False
            c = True
        a += d
        d += 1
    print(a-1)
# ça ne marche pas, trop compliqué sans avoir recours aux bibliothèques

def b():
    i = 1
    while True:
        triangle = sum(range(1,i+1))
        i += 1
        if len(divisors(triangle)) > 500:
            print(triangle)
            break

b()

# c'est la correction, ça marche bien on est content 
