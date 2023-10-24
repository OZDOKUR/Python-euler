def factorialOfTheSum(factorNum):
    if factorNum == 0 or factorNum == 1:
        return 1
    else:
        return factorNum * factorialOfTheSum(factorNum - 1)
gridLen = 20
gridSize = 20
sumOfFactorail = factorialOfTheSum(gridLen+gridSize)
productOfFactorial = factorialOfTheSum(gridLen)*factorialOfTheSum(gridSize)
total = format(int(sumOfFactorail/productOfFactorial),",")
print(f"This Grid is {gridSize}x{gridLen} and {total} route ")
