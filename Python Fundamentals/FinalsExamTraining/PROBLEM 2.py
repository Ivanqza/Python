import re

pattern = r"(.+)>\d{3}\|[a-z]{3}\|[A-Z]{3}\|[^<>]{3}<(\1)"

number_of_inputs = int(input())
for i in range(number_of_inputs):
    password = input()
    matches = [match.groupdict() for match in re.finditer(pattern, password)]
    if matches:
        final_string = password[password.find(">") + 1: password.find("<")]
        final_string = final_string.replace("|", "", 3)
        print(f"Password: {final_string}")
    else:
        print("Try another password!")