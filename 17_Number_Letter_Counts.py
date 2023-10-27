"""1'den 5'e kadar olan sayılar bir, iki, üç, dört, beş şeklinde yazıyla yazılırsa toplamda 3+3 +5+4+4= 19 harf kullanılır.
1'den 1000 (bin)'e kadar olan sayıların tamamı yazıyla yazılsaydı kaç harf kullanılırdı?
NOT: Boşlukları veya kısa çizgileri saymayın. Örneğin 342 (üç yüz kırk iki) sayısında 23 harf, 115 (yüz on beş) sayısında ise 20 harf bulunmaktadır. Sayıları yazarken "ve" kullanımı İngiliz kullanımına uygundur.
"""
def numberToWords(n):
    units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
             "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen",
             "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    if n < 20:
        return units[n]
    elif n < 100:
        return tens[n // 10] + units[n % 10]
    elif n < 1000:
        if n % 100 == 0:
            return units[n // 100] + "hundred"
        else:
            return units[n // 100] + "hundredand" + numberToWords(n % 100)
    elif n == 1000:
        return "onethousand"

totalLength = 0

for i in range(1, 1001):
    word = numberToWords(i)
    totalLength += len(word)

print(totalLength)