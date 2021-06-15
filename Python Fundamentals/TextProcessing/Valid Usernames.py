allowed_chars = set("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-")
users = input().split(", ")
valid_usernames = []
for user in users:
    validation = set(user)
    if validation.issubset(allowed_chars) and (3 < len(user) < 16):
        print(user)



