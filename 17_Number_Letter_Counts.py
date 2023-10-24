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