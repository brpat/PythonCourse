# Generator function to calculate fibonacii sequence
def fib(num):
    num1 = 0
    num2 = 1
    for i in range(num + 2):
        if (i == 0 or i == 1):
            yield 1
        else:
            tmp = num1
            num1 = num1 + num2
            num2 = tmp
            yield num1


for val in fib(20):
    print(val)