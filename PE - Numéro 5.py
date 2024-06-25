a = 2
while True:
    if all(a % n == 0 for n in range(1,20)):
        print(a)
        break
    else:
        a += 2 
# ce code prend 5 minutes à se termier environ (et c'est le plus rapide !)