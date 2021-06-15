import re

text = input()
pattern = r"(?P<Day>\d{2})(?P<Separator>[\.\-\/])(?P<Month>[A-Z][a-z]{2})(?P=Separator)(?P<Year>\d{4})"

valid_dates = [match_obj.groupdict() for match_obj in re.finditer(pattern, text)]
print('\n'.join([f"Day: {data['Day']}, Month: {data['Month']}, Year: {data['Year']}" for data in valid_dates]))