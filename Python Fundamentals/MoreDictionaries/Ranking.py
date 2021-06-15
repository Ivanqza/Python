command = input()

contests_and_passwords_dict = {}
users_and_points_dict = {}

while not command == "end of contests":
    contest, password_for_contest = command.split(":")
    contests_and_passwords_dict[contest] = password_for_contest

    command = input()

username_and_points = input()

while not username_and_points == "end of submissions":
    contest_submission, password_of_contest, username, points = username_and_points.split("=>")
    points = int(points)

    if contest_submission in contests_and_passwords_dict:
        if password_of_contest == contests_and_passwords_dict[contest_submission]:
            if username not in users_and_points_dict:
                users_and_points_dict[username] = {}
                if contest_submission not in users_and_points_dict[username]:
                    users_and_points_dict[username][contest_submission] = points
                else:
                    if users_and_points_dict[username][contest_submission] < points:
                        users_and_points_dict[username][contest_submission] = points

            else:
                if contest_submission not in users_and_points_dict[username]:
                    users_and_points_dict[username][contest_submission] = points
                else:
                    if users_and_points_dict[username][contest_submission] < points:
                        users_and_points_dict[username][contest_submission] = points

    username_and_points = input()

sorted_dict = dict(sorted(users_and_points_dict.items(), key=lambda kvp: kvp[0]))

total_points = 0
max_points = 0
max_points_username = ""

for username, dictionary in sorted_dict.items():
    for key, value in sorted_dict[username].items():
        total_points += value
    if max_points < total_points:
        max_points = total_points
        max_points_username = username
        total_points = 0

print(f'Best candidate is {max_points_username} with total {max_points} points.')
print('Ranking:')

for username, dictionary in sorted_dict.items():
    print(f"{username}")
    scores = sorted(sorted_dict[username].items(), key=lambda kvp: kvp[1], reverse=True)
    for key, value in scores:
        print(f"# {key} -> {value}")
