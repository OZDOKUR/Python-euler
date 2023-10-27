"""
İlk altı asal sayıyı listeleyerek: 2, 3, 5, 7, 11, ve 13, 6. asalın 13 olduğunu görebiliriz.

10001. asal sayı nedir?
"""
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def findNthPrime(n):
    count = 0
    number = 2
    while count < n:
        if isPrime(number):
            count += 1
        if count == n:
            return number
        number += 1

nthPrime = findNthPrime(10001)
print(nthPrime)