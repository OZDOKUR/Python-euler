"""
Palindromik bir sayı her iki yönde de aynı şeyi okur.
İki 2 basamaklı sayının ürününden yapılan en büyük palindrom
9009 = 91 × 99'dur.
İki 3 basamaklı sayının ürününden yapılan en büyük palindromu bulun.
"""
def palindrome(number):
    return str(number) == str(number)[::-1]

largestPalindrome = 0

for i in range(100,1000):
    for j in range(100,1000):
        sum=i*j
        if palindrome(sum) and sum > largestPalindrome:
            largestPalindrome=sum
            number1=i
            number2=j
print(number1,"*",number2,"=",largestPalindrome)