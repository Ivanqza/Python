text = input()

for index in range(0, len(text)):
    if text[index] == ":":
        emoticon = f"{text[index]}{text[index+1]}"
        print(emoticon)
