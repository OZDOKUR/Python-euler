"""
Size aşağıdaki bilgiler verilmiştir, ancak kendiniz için biraz araştırma yapmayı tercih edebilirsiniz.
-1 Ocak 1900 Pazartesi'ydi.
-Otuz gün Eylül var,
Nisan, Haziran ve Kasım.
Geri kalanların hepsinde otuz bir var,
Şubat ayını tek başına kurtarmak,
Yirmi sekizi var, yağmur ya da güneş.
Ve artık yıllarda yirmi dokuz.
-Artık yıl, 4'e eşit olarak bölünebilen herhangi bir yılda oluşur, ancak 400'e bölünemeyen bir yüzyılda olmaz.

Yirminci yüzyılda (1 Ocak 1901'den 31 Aralık 2000'e kadar) ayın ilk günü kaç Pazar'a denk geliyordu?
"""
import datetime

startDate = datetime.date(1901, 1, 1)
endDate = datetime.date(2000, 12, 31)

count = 0

while startDate <= endDate:
    if startDate.weekday() == 6:
        count += 1
    startDate += datetime.timedelta(days=1)

print("The number of months that fall on a Sunday =",count)
