"""
215 = 32768 ve rakamlarının toplamı 3+2+7+6+8 = 26'dır.
21000 sayısının rakamlarının toplamı kaçtır?
"""
number = 2**1000
digits = []

while number > 0:
    digit = number % 10
    digits.insert(0, digit)
    number = number // 10
powerDigitSum = sum(digits)
print(powerDigitSum)