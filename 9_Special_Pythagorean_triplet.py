"""
#EN
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2+b^2=c^2
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
#TR
Pisagor üçlüsü, üç doğal sayıdan oluşan bir kümedir, a < b < c, bunun için,
a^2+b^2=c^2
a + b + c = 1000 olan tam olarak bir Pisagor üçlüsü vardır.Abc ürününü bulun.
"""
def product():
    for a in range (1,1001):
        for b in range(a+1,1001):
            c=1000-a-b
            if a**2 + b**2 == c**2:
                return a,b,c
print(product())