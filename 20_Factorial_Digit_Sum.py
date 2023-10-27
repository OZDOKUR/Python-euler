"""
N! n x (n − 1) x ... × 3 × 2 × 1 anlamına gelir.

Örneğin 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
ve 10! sayısının rakamlarının toplamı 3+6+2+8+8+0 +0 = 27'dir.
100! sayısının rakamlarının toplamını bulun.
"""

import math

num = 100
factorial = math.factorial(num)
digitSum = sum(int(digit) for digit in str(factorial))

print("The sum of the digits of the 100 factorial is:", digitSum)