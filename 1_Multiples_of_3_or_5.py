"""
EN
If we list all the natural numbers below 10 that are multiples of 3 or 5
We get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""
#TR
#10'un altındaki 3 veya 5'in katları olan tüm doğal sayıları listelersek
#3, 5, 6 ve 9 elde ederiz. Bu katların toplamı 23'tür.
#1000'in altındaki 3 veya 5'in tüm katlarının toplamını bulun.

sum=0
for number in range (1,1000):
    if number%3==0 or number%5==0:
        sum+=number
print(sum)
