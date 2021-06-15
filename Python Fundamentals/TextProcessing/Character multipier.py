string1, string2 = input().split()
sum = 0

if len(string1) == len(string2):
    for index in range(0, len(string1)):
        sum += ord(string1[index]) * ord(string2[index])

elif len(string1) > len(string2):
    for index in range(0, len(string2)):
        sum += ord(string1[index]) * ord(string2[index])
    rest = string1[len(string2):]
    for x in rest:
        sum += ord(x)

else:
    for index in range(0, len(string1)):
        sum += ord(string1[index]) * ord(string2[index])
    rest = string2[len(string1):]
    for x in rest:
        sum += ord(x)

print(sum)