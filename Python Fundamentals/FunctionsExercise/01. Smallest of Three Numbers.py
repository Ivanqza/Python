def the_smallest_number(number1, number2, number3):
    smallest_number = min(num1, num2, num3)
    return smallest_number


num1 = int(input())
num2 = int(input())
num3 = int(input())
result = the_smallest_number(num1, num2, num3)
print(result)
