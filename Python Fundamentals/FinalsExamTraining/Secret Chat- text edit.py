message = input()
data = input()

while not data == "Reveal":
    command = data.split(":|:")
    if command[0] == "ChangeAll":
        to_remove, to_replace = command[1], command[2]
        if to_remove in message:
            message = message.replace(to_remove, to_replace)
            print(message)
    elif command[0] == "Reverse":
        to_reverse = command[1]
        if to_reverse in message:
            message = message.replace(to_reverse, '', 1)
            new_message = to_reverse[::-1]
            message = message + new_message
            print(message)
        else:
            print("error")
    elif command[0] == "InsertSpace":
        index = int(command[1])
        left_side = message[:index]
        right_side = message[index:]
        message = left_side + " " + right_side
        print(message)
    data = input()

print(f"You have a new text message: {message}")