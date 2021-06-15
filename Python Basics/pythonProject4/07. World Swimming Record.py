current_record = float(input())
distance = float(input())
time_per_meter_in_seconds = float(input())
delay = distance // 15 * 12.5
new_time = distance * time_per_meter_in_seconds + delay
if new_time < current_record:
    print(f"Yes, he succeeded! The new world record is {new_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {(new_time - current_record):.2f} seconds slower.")
