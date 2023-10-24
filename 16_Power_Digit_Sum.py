number = 2**1000
digits = []

while number > 0:
    digit = number % 10
    digits.insert(0, digit)
    number = number // 10
powerDigitSum = sum(digits)
print(powerDigitSum)