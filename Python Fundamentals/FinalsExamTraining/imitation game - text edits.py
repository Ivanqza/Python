encrypted_message = input()
data = input()
while not data == "Decode":
    command = data.split("|")
    if command[0] == "Move":
        letter_to_move = int(command[1])
        left = encrypted_message[0:letter_to_move]
        right = encrypted_message[letter_to_move:]
        encrypted_message = right + left
    if command[0] == "Insert":
        insert_after = int(command[1])
        text_to_insert = command[2]
        left = encrypted_message[0:insert_after]
        right = encrypted_message[insert_after:]
        encrypted_message = left + text_to_insert + right
    if command[0] == "ChangeAll":
        replace = command[1]
        replace_with = command[2]
        encrypted_message = encrypted_message.replace(replace, replace_with)
    data = input()
print(f"The decrypted message is: {encrypted_message}")