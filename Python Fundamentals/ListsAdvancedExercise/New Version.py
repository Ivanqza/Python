version_as_list = input().split(".")
version_as_int = int("".join(version_as_list)) +1
new_version = list(str(version_as_int))

print(".".join(new_version))

