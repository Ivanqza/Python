text = input()
new_text = ""

for char in text:
    current_char = ord(char)
    new_char = current_char + 3
    new_text += chr(new_char)

print(new_text)