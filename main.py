def bringNumbersSum(a):
    a=str(a)
    numbersSum=0
    for i in range(0,len(a)):
        numbersSum += int(a[i])
    return numbersSum

def bringUpTheSumOfPrimeFactors(num):
    sumPrimeFactors=0
    divide=2
    while num != 1:
        if num % divide == 0:
            num=num/divide
            sumPrimeFactors+=bringNumbersSum(divide)
            divide=divide-1
        divide=divide+1
    return sumPrimeFactors

num = int(input("Enter a control number: "))
num=int(num)

if bringUpTheSumOfPrimeFactors(num) == bringNumbersSum(num):
    print("{0} is number of Smith.".format(num))
else:
    print("{0} is not number of Smith.".format(num))