command = input()
sum_of_prime_numbers = 0
sum_of_non_prime_numbers = 0

while command != "stop":
    is_prime = True
    current_number = int(command)
    for number in range(2, current_number):
        if current_number % number == 0 and current_number > 2:
            is_prime = False
            break
    if current_number < 0:
            print("Number is negative.")
    else:
         if is_prime:
             sum_of_prime_numbers += current_number
         else:
             sum_of_non_prime_numbers += current_number

    command = input()
print(f"Sum of all prime numbers is: {sum_of_prime_numbers}")
print(f"Sum of all non prime numbers is: {sum_of_non_prime_numbers}")