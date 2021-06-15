command = input()
course_dict = {}
users_dict = {}
position = 1

while not command == "no more time":
    username, course, points = command.split(" -> ")
    points = int(points)
    if course not in course_dict:
        course_dict[course] = {username: points}
        if username not in users_dict:
            users_dict[username] = points
        else:
            users_dict[username] += points
    else:
        if username not in course_dict[course]:
            course_dict[course][username] = points
            if username not in users_dict:
                users_dict[username] = points
            else:
                users_dict[username] += points
        else:
            if course_dict[course][username] < points:
                users_dict[username] += points - course_dict[course][username]
                course_dict[course][username] = points
    command = input()

for course, dict in course_dict.items():
    print(f"{course}: {len(course_dict[course])} participants")
    scores = sorted(course_dict[course].items(), key=lambda x: (-x[1], x[0]))
    for key, value in scores:
        print(f"{position}. {key} <::> {value}")
        position += 1
    position = 1

print(f"Individual standings:")
total_points = sorted(users_dict.items(), key=lambda x: (-x[1], x[0]))
for key, value in total_points:
    print(f"{position}. {key} -> {value}")
    position += 1
position = 1

