import math

num = 100
factorial = math.factorial(num)
digitSum = sum(int(digit) for digit in str(factorial))

print("The sum of the digits of the 100 factorial is:", digitSum)