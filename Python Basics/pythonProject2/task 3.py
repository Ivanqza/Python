deposit = float(input())
months = int(input())
interest_rate = float(input())
print(deposit + months * ((deposit * interest_rate / 100) / 12))
