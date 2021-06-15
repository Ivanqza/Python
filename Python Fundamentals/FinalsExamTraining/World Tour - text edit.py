destination = input()
data = input()

# command.startswith("Add") also works instead of if command == "Add Stop":


while not data == "Travel":
    command, val_1, val_2 = data.split(":")
    if command == "Add Stop":
        add_after = int(val_1)
        if len(destination) > add_after:
            add_stop = val_2
            left_side = destination[:add_after]
            right_side = destination[add_after:]
            destination = left_side + add_stop + right_side
    elif command == "Remove Stop":
        start = int(val_1)
        end = int(val_2)
        if len(destination) > start and len(destination) > end:
            edit = destination[start:end]
            left_part = destination[:start]
            right_part = destination[end+1:]
            destination = left_part + right_part
    elif command == "Switch":
        if val_1 in destination:
            replace = val_1
            replace_with = val_2
            destination = destination.replace(replace, replace_with)
    print(destination)
    data = input()

print(f"Ready for world tour! Planned stops: {destination}")
