def moveRight(current_index, result):
    index_to_move = result[current_index]
    index_to_switch = result[current_index + 1]
    result[current_index] = index_to_switch
    result[current_index + 1] = index_to_move
    return result


def moveLeft(current_index, result):
    index_to_move = result[current_index]
    index_to_switch = result[current_index-1]
    result[current_index] = index_to_switch
    result[current_index-1] = index_to_move
    return result

def check_if_odd(particles):
    result = ""
    for odd in range(1, len(particles), 2):
        result += particles[odd] + " "
    return result

def check_if_even(particles):
    result = ""
    for odd in range(0, len(particles), 2):
        result += particles[odd] + " "
    return result


particles = input().split("|")
command_data = input()


while not command_data == "Done":
    if "Move Left" in command_data:
        splitted_common_data = command_data.split()
        index = int(splitted_common_data[2])
        if index-1 >= 0 and index <= len(particles):
            particles = moveLeft(index, particles)
    elif "Move Right" in command_data:
        splitted_common_data = command_data.split()
        index = int(splitted_common_data[2])
        if index+1 <= len(particles)-1 and index >= 0:
            particles = moveRight(index, particles)
    elif "Check Odd" in command_data:
        print(check_if_odd(particles))
    elif "Check Even" in command_data:
        print(check_if_even(particles))

    command_data = input()

s = "".join(particles)
print(f"You crafted {s}!")
