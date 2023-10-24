"""
#EN
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

#TR
10'un altındaki asal sayıların toplamı 2 + 3 + 5 + 7 = 17.

İki milyonun altındaki tüm asal sayıların toplamını bulun.
"""
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def sumOfPrimes(limit):
    prime_sum = 0
    for num in range(2, limit):
        if isPrime(num):
            prime_sum += num
    return prime_sum

limit = 2000000
result = sumOfPrimes(limit)
print(result)