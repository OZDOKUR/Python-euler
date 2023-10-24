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
