def prime(num):
    for i in range(2, int((num**0.5))+1):
        if not num % i:
            return False
    return True
result = 2
for i in range(3, 2000000, 2):
    if prime(i):
        result += i
print(result)