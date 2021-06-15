def transform(one, two):
    if one == "int":
        result = int(two) * 2
        print(result)
    elif one == "real":
        result = float(two) * 1.5
        print(f"{result:.2f}")
    elif one == "string":
        print(f"${two}$")


first_line = input()
second_line = input()
transform(first_line, second_line)