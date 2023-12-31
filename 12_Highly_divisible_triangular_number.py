"""
Üçgen sayılar dizisi, doğal sayılar eklenerek oluşturulur. Yani 7. üçgen sayısı şöyle olurdu;
1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. İlk on terimi de şöyle olurdu:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

İlk yedi üçgen sayının faktörlerini listeleyelim:

1: 1
3: 1,3
6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
28'in beşten fazla bölene sahip ilk üçgen sayı olduğunu görebiliriz.

Beş yüzden fazla bölene sahip olan ilk üçgen sayısının değeri nedir?
"""
def triangleNumber(n):
    return (n * (n + 1)) // 2

def divisorCount(num):
    count = 0
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            count += 2
    if num**0.5 == int(num**0.5):
        count -= 1
    return count

targetDivisors = 500
currentNum = 1
while True:
    triangleNum = triangleNumber(currentNum)
    divisors = divisorCount(triangleNum)
    if divisors > targetDivisors:
        break
    currentNum += 1

print("First triangle number:", triangleNum)
print("The number of divisibility:", divisors)
