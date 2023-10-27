"""Pozitif tamsayılar kümesi için aşağıdaki yinelemeli dizi tanımlanır:
n → n/2 (n çifttir)
n→ 3n+ 1 (n tektir)
Yukarıdaki kuralı kullanarak ve 13'ten başlayarak aşağıdaki diziyi oluştururuz:
13 → 40 → 20 → 105 → 16 → 84 → 2 → 1.
Bu dizinin (13'ten başlayıp 1'de biten) 10 terim içerdiği görülmektedir. Henüz kanıtlanamasa da (Collatz Problemi) tüm başlangıç ​​sayılarının 1'de bittiği düşünülmektedir.
Bir milyonun altındaki hangi başlangıç ​​numarası en uzun zinciri oluşturur?
NOT: Zincir başladıktan sonra terimlerin bir milyonun üzerine çıkmasına izin verilir.
"""

def collatzProblem(number):
    array = []
    array.append(number)
    while number != 1:
        if number%2 == 0:
            number = number/2
            array.append(number)    
        else:
            number = (3*number)+1
            array.append(number)
    return len(array)
value = 0

for i in range(1,1000001):
    maxlen = collatzProblem(i)
    if maxlen >= value:
        value = maxlen
        counter = i
    else:
        continue
print("Chain Len:",value,"\n Number:",counter)
