def subtract(summed_result, n3):
    return summed_result - n3


def sum_number(n1, n2):
    result1 = n1 + n2
    result2 = subtract(result1, num3)
    return result2


num1 = int(input())
num2 = int(input())
num3 = int(input())
final_result = sum_number(num1, num2)
print(final_result)
