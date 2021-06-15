most_powerful_word = " "
max_power = 0
command = input()

while command != "End of words":
    current_word = command
    current_power = 0
    for letter in current_word:
        current_power += ord(letter)
    must_be_multiplied = False
    if current_word[0] == "a" or current_word[0] == "A":
        must_be_multiplied = True
    elif current_word[0] == "e" or current_word[0] == "E":
        must_be_multiplied = True
    elif current_word[0] == "i" or current_word[0] == "I":
        must_be_multiplied = True
    elif current_word[0] == "o" or current_word[0] == "O":
        must_be_multiplied = True
    elif current_word[0] == "u" or current_word[0] == "U":
        must_be_multiplied = True
    elif current_word[0] == "y" or current_word[0] == "Y":
        must_be_multiplied = True
    if must_be_multiplied:
        current_power *= len(current_word)
    else:
        current_power = int(current_power / len(current_word))
    if current_power > max_power:
        max_power = current_power
        most_powerful_word = current_word
    command = input()
print(f"The most powerful word is {most_powerful_word} - {max_power}")
