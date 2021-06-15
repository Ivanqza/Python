data = input()

records = {}
while not data == "Log out":
    splitted_data = data.split(": ")
    command = splitted_data[0]
    username = splitted_data[1]
    if command == "New follower":
        if username not in records:
            records[username] = {"likes": 0, "comments": 0}
    elif command == "Like":
        count = int(splitted_data[2])
        if username not in records:
            records[username] = {"likes": count, "comments": 0}
        else:
            records[username]["likes"] += count
    elif command == "Comment":
        if username not in records:
            records[username] = {"likes": 0, "comments": 1}
        else:
            records[username]["comments"] += 1
    elif command == "Blocked":
        if username not in records:
            print(f"{username} doesn't exist.")
        else:
            records.pop(username)

    data = input()

print(f"{len(records)} followers")
for name, values in sorted(records.items(), key=lambda kvp: (-(kvp[1]["likes"] + kvp[1]["comments"]), kvp[0])):
    total = values["likes"] + values["comments"]
    print(f"{name}: {total}")