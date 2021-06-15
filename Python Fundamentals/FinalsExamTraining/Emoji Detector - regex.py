import re


def multiplyList(mylist):
    result = 1
    for x in mylist:
        result = result * x
    return result


def emoji_sum_and_split(emojis):
    summed = 0
    for x in emojis:
        emoji = x[2:-2]
        emoji_split = [c for c in emoji]
        for y in emoji_split:
            summed += ord(y)
        if summed >= cool_threshold:
            is_cool.append(x)
        summed = 0
    return is_cool


text = input()
is_cool = []
emoji_pattern = r"((\:{2})[A-Z][a-z][a-z]+(\:{2})|(\*{2})[A-Z][a-z][a-z]+(\*{2}))"
digit_pattern = r"\d"

digits = [int(el) for el in re.findall(digit_pattern, text)]
emojis = [el.group() for el in re.finditer(emoji_pattern, text)]
cool_threshold = multiplyList(digits)


print(f"Cool threshold: {cool_threshold}")
print(f"{len(emojis)} emojis found in the text. The cool ones are:")
print("\n".join(emoji_sum_and_split(emojis)))
