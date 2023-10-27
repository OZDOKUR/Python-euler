"""
2x2'lik bir gridin sol üst köşesinden başlayıp sadece sağa ve aşağıya doğru hareket edebilen, sağ alt köşeye giden tam 6 yol var.
20 × 20'lik bir ızgarada bu şekilde kaç tane rota vardır?
"""
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
