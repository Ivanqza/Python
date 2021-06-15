activation_code = input()

while True:
    command = input()
    splitted_command = command.split(">>>")
    order = splitted_command[0]
    if order == "Contains":
        if splitted_command[1] in activation_code:
            print(f"{activation_code} contains {splitted_command[1]}")
        else:
            print(f"Substring not found!")
    if order == "Flip":
        start = int(splitted_command[2])
        end = int(splitted_command[3])
        if splitted_command[1] == "Upper":
            edit = activation_code.upper()[start:end]
            left_part = activation_code[0:start]
            right_part = activation_code[end:]
            activation_code = left_part + edit + right_part
            print(activation_code)
        elif splitted_command[1] == "Lower":
            edit = activation_code.lower()[start:end]
            left_part = activation_code[0:start]
            right_part = activation_code[end:]
            activation_code = left_part + edit + right_part
            print(activation_code)
    if order == "Slice":
        start = int(splitted_command[1])
        end = int(splitted_command[2])
        edit = activation_code[start:end]
        left_part = activation_code[0:start]
        right_part = activation_code[end:]
        activation_code = left_part + right_part
        print(activation_code)

    if order == "Generate":

        print(f"Your activation key is: {activation_code}")
        break