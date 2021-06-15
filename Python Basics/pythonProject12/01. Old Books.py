book_name = input()
book_count = 0
is_book_found = False
current_book = input()

while current_book != "No More Books":
    if current_book == book_name:
        is_book_found = True
        break
    book_count += 1
    current_book =input()

if is_book_found:
    print(f"You checked {book_count} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {book_count} books.")