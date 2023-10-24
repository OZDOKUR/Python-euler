"""
#EN
Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose
values do not exceed four million, find the sum of the even-valued terms.
#TR
Fibonacci dizisindeki her yeni terim,önceki iki terim eklenerek oluşturulur.
1 Ve 2 ile başlayarak, ilk 10 terim şöyle olacaktır:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
Değerleri dört milyonu geçmeyen Fibonacci dizisindeki terimleri göz önünde 
bulundurarak, çift değerli terimlerin toplamını bulun.
"""
fib = [0, 1]
evenSum = 0
while fib[-1] <= 4000000:
    fib.append(fib[-1] + fib[-2])
    if fib[-1] % 2 == 0:
            evenSum += fib[-1]
print(evenSum)
