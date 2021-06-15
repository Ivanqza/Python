import math
gpu_price = int(input())
connector_price = int(input())
electricity_bill_per_gpu = float(input())
profit_by_gpu = float(input())
initial_investment = 1000

total_price_of_gpu = gpu_price * 13
total_price_of_connector = connector_price * 13
total_investment = total_price_of_connector + total_price_of_gpu + initial_investment
profit_per_gpu_per_day = profit_by_gpu - electricity_bill_per_gpu
profit_per_day = profit_per_gpu_per_day * 13
days_of_return = math.ceil(total_investment / profit_per_day)

print(total_investment)
print(days_of_return)