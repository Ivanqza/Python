note = input()

todo_list = [0] * 10

while not note == "End":
    importance, task = note.split("-")
    importance = int(importance)
    todo_list[importance] = task
    note = input()

print([task for task in todo_list if not task == 0])
