def calc_factorial(num):
    factorial = 1
    for n in range(2, num + 1):
        factorial *= n
    return factorial


def get_factorial_divisions(f1, f2):
    return f1 / f2


num1 = int(input())
num2 = int(input())
fact1 = calc_factorial(num1)
fact2 = calc_factorial(num2)

result = get_factorial_divisions(fact1, fact2)
print(f"{result:.2f}")
