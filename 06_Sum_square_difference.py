"""
İlk on doğal sayının karelerinin toplamı,
1^2+2^2+3^2....+10^2=385
İlk on doğal sayının toplamının karesi,
(1+2+....+10)^2=55^2=3025
Bu nedenle, ilk on doğal sayının karelerinin toplamı ile
toplamın karesi arasındaki fark
3025-385=2640
İlk yüz doğal sayının karelerinin toplamı ile toplamın karesi arasındaki farkı bulun.
"""
squareOfSum=sum(range(1, 101))**2
sumOfSquares = sum([i**2 for i in range(1, 101)])
finalSum=squareOfSum-sumOfSquares
print(finalSum)