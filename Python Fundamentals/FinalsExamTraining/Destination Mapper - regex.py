import re


pattern = r"(?<=(/|\=))[A-Z][a-zA-Z][a-zA-Z]+(?=\1)"
text = input()

matches = [d.group() for d in re.finditer(pattern, text)]

travel_points = sum([len(d) for d in matches])
print(f"Destinations: {', '.join(matches)}")
print(f"Travel Points: {travel_points}")