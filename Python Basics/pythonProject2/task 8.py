length = int(input())
width = int(input())
height = int(input())
occupied_volume = float(input())
volume_of_aquarium = length * width * height
total_liters = volume_of_aquarium * 0.001
percentage_of_occupied_volume = occupied_volume * 0.01
liters_required = total_liters * (1-percentage_of_occupied_volume)
print(liters_required)
