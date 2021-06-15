command = input()

chat_log = []

while not command == "end":
    if "Chat" in command:
        splitted_command = command.split()
        chat_log.append(splitted_command[1])
    elif "Delete" in command:
        splitted_command = command.split()
        chat_log.remove(splitted_command[1])
    elif "Edit" in command:
        splitted_command = command.split()
        index = chat_log.index(splitted_command[1])
        chat_log[index] = splitted_command[2]
    elif "Pin" in command:
        splitted_command = command.split()
        index = chat_log.index(splitted_command[1])
        chat_log.append(chat_log.pop(index))
    elif "Spam" in command:
        splitted_command = command.split()
        for index in range(1, len(splitted_command)):
            chat_log.append(splitted_command[index])

    command = input()
print("\n".join(chat_log))