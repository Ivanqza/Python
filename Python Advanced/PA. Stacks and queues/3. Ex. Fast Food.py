from collections import deque

total_food = int(input())
order_queue = deque()

for order in input().split():
    order_queue.append(int(order))

max_order = max(order_queue)

for item in range(len(order_queue)):
    order = order_queue.popleft()
    if order <= total_food:
        total_food = total_food - order
    else:
        order_queue.appendleft(order)
        break

print(max_order)
if len(order_queue) == 0:
    print('Orders complete')
else:
    print('Orders left:', ' '.join([str(order) for order in order_queue]))