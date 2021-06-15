import re

pattern = r"(?P<separator>@|#)(?P<word1>[A-Za-z]{3,})(?P=separator)(?P=separator)(?P<word2>[A-Za-z]{3,})(?P=separator)"

text = input()
matches = [match.groupdict() for match in re.finditer(pattern, text)]

if not matches:
    print(f"No word pairs found!")
    print(f"No mirror words!")
else:
    print(f"{len(matches)} word pairs found!")
    mirror_words = {}
    for match in range(len(matches)):
        if matches[match]['word1'] == matches[match]['word2'][::-1]:
            mirror_words[f"Pair {match + 1}"] = matches[match]['word1'], matches[match]['word2']

    if mirror_words:
        print("The mirror words are:")
        list_of_words = []
        for x, y in mirror_words.items():
            list_of_words.append(f"{y[0]} <=> {y[1]}")
        print(*list_of_words, sep=", ")
    else:
        print(f"No mirror words!")
