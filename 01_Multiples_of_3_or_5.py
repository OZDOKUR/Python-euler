"""10'un altındaki 3 veya 5'in katları olan tüm doğal sayıları listelersek
3, 5, 6 ve 9 elde ederiz. Bu katların toplamı 23'tür.
1000'in altındaki 3 veya 5'in tüm katlarının toplamını bulun.
"""
sum=0
for number in range (1,1000):
    if number%3==0 or number%5==0:
        sum+=number
print(sum)
