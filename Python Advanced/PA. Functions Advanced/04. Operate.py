from functools import reduce


# def operate(operator, *args):
#     if operator == '+':
#         return reduce(lambda x, y: x+y, args)
#     elif operator == '-':
#         return reduce(lambda x, y: x-y, args)
#     elif operator == '*':
#         return reduce(lambda x, y: x*y, args)
#     else:
#         return reduce(lambda x, y: x/y, args)
#
#
# print(operate('+', 1, 2, 3))


def operate(operator, *args):
    return reduce(lambda x, y: eval(f"{x} {operator} {y}"), args)


print(operate('+', 1, 2, 3))
# ЕДНАКВО, НО ПЪРВОТО Е ПО-ПАЙТЪНСКО
# print(*[1, 2, 3], sep="->")
# print("->".join(["1", "2", "3"]))
