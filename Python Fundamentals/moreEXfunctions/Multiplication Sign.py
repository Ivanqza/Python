def fun_positive_negative(f1, f2, f3):
    if f1 == 0 or f2 == 0 or f3 == 0:
        print("zero")
    elif f1 > 0 and f2 > 0 and f3 > 0:
        print("positive")
    elif f1 < 0 and f2 < 0 and f3 > 0:
        print("positive")
    elif f1 < 0 and f2 > 0 and f3 < 0:
        print("positive")
    elif f1 > 0 and f2 < 0 and f3 < 0:
        print("positive")

    else:
        print("negative")


num1 = int(input())
num2 = int(input())
num3 = int(input())

rez = fun_positive_negative(num1, num2, num3)