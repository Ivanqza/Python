import os

# try:
#     os.remove('to_remove.txt')
# except FileNotFoundError:
#     print('File already deleted')


if os.path.exists('to_remove.'):
    os.remove('to_remove')
else:
    print('File already deleted')