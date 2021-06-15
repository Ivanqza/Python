def odd_string(x):
    return x[1::2]


password = input()
data = input()
while not data == "Done":
    data = data.split()
    if data[0] == "TakeOdd":
        password = odd_string(password)
        print(password)
    elif data[0] == "Cut":
        index = int(data[1])
        length = int(data[2])
        to_remove = password[index:index + length]
        password = password.replace(to_remove, "", 1)
        print(password)
    elif data[0] == "Substitute":
        to_remove = data[1]
        replace_with = data[2]
        if to_remove in password:
            password = password.replace(to_remove, replace_with)
            print(password)
        else:
            print(f"Nothing to replace!")
    data = input()

print(f"Your password is: {password}")
