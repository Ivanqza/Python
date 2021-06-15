n = int(input())
all_guests = set()

for _ in range(n):
    all_guests.add(input())

ticket = input()
arrived = set()

while not ticket == "END":
    arrived.add(ticket)
    ticket = input()

difference = all_guests.difference(arrived)

print(len(difference))

for guest in sorted(difference):
    if guest[0].isdigit():
        print(guest)
for guest in sorted(difference):
    if guest[0].isalpha():
        print(guest)