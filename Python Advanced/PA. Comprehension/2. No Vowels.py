# word = input()
#
# print("".join([char for char in word if char not in 'aouei' and char not in 'AOUEI']))
#
# or char.lower !!!!
def is_vowel(char):
    if char not in 'aoueiAOUEI':
        return True
    return False


print("".join([char for char in input() if is_vowel(char)]))
