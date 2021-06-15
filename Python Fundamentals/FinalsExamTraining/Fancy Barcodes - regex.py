import re

pattern = r"(@#+)[A-Z][A-Za-z0-9]{4,}[A-Z](@#+)"
digits = r"\d"
n = int(input())
for _ in range(n):
    string = input()
    matches = [match.group() for match in re.finditer(pattern, string)]
    if matches:
        group = "00"
        match_digits = re.findall(digits, string)
        if match_digits:
            group = "".join(match_digits)
        print(f"Product group: {group}")
    else:
        print(f"Invalid barcode")