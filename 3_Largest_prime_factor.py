"""
#EN
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?

#TR
13195'in asal faktörleri 5, 7, 13 ve 29'dur.
600851475143 sayısının en büyük asal faktörü nedir?
"""
def largestPrimeFactor(number):
    i = 2
    while i * i <= number:
        if number % i:
            i += 1
        else:
            number //= i
    if number > 1:
        return number
    else:
        return i
number = 600851475143
largestPrime = largestPrimeFactor(number)
print(largestPrime) 
