from os import path

if path.exists('text.txt'):
    print('File found')
else:
    print('File not found')


# second
# try:
#     open('text.txt')
#     print('File found')
# except FileNotFoundError:
#     print('File not found')