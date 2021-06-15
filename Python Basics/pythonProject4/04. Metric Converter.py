number = float(input())
input_currency = input()
output_currency = input()

if input_currency == "cm":
    number = number * 10  # number *= 10
elif input_currency == "m":
    number *= 1000   # number = number * 1000

if output_currency == "cm":
    number /= 10  # number = number / 10
elif output_currency == "m":
    number /= 1000  # number = number / 1000

print(f"{number:.3f}")