import re

pattern = r"(.+)>\d{3}\|[a-z]{3}\|[A-Z]{3}\|[^<>]{3}<(\1)"

num_inputs = int(input())
for i in range(num_inputs):
    password = input()
    if re.fullmatch(pattern, password):
        conc_string = password[password.find(">")+1:password.find("<")]
        conc_string = conc_string.replace("|", "", 3)
        print(f"Password: {conc_string}")
    else:
        print("Try another password!")