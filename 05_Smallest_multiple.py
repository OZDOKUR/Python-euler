"""
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