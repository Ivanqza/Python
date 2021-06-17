with open('input.txt') as file:
    lines = [line.strip() for line in file.readlines()]

out = []

for idx, line in enumerate(lines):
    letter_counter = (sum([len(word) for word in line.split()]))
    punct_counter = (sum([1 for word in line.split() for letter in word if letter in r'-,\.!?\'']))

    out.append(f'Line {idx + 1}: {line} ({letter_counter - punct_counter})({punct_counter})')


with open('outputex.txt', 'w') as output_file:
    output_file.writelines([line + '\n' for line in out])