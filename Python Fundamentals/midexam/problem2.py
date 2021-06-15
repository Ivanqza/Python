particles = input().split("|")
command_data = input()

while not command_data == "Done":
    command_data = command_data.split()
    if "Move Left" in command_data:
        index = command_data[2]
        particles.insert(index-1, particles.pop(index))
    elif "Move Right" in command_data:
        index = command_data[2]
        particles.insert(index+1, particles.pop(index))

