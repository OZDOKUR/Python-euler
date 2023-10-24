"""
#EN
2520 is the smallest number that can be divided by each of the numbers from
1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers 
from 1 to 20?

#TR
2520, kalan olmadan 1'den 10'a kadar olan sayıların her birine bölünebilen
en küçük sayıdır.
1'den 20'ye kadar olan tüm sayılarla eşit olarak bölünebilen en küçük pozitif 
sayı nedir?
"""
def findSmallestMultiple():
    number = 1
    while True:
        divisible = True
        for i in range(1, 11):
            if number % i != 0:
                divisible = False
                break
        if divisible:
            return number
        number += 1
print(findSmallestMultiple())