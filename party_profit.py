import math

group_size = int(input())
days = int(input())
earn_money = 0
for i in range(1, days + 1):
    if i % 10 == 0:
        group_size -= 2
    if i % 15 == 0:
        group_size += 5

    if i % 3 == 0 and i % 5 != 0:
        earn_money += (50 - 5 * group_size)
    elif i % 5 == 0 and i % 3 != 0:
        earn_money += (20 * group_size)
        earn_money += (50 - 2 * group_size)
    elif i % 5 == 0 and i % 3 == 0:
        earn_money += (20 * group_size)
        earn_money += (50 - 7 * group_size)
    else:
        earn_money += (50 - 2 * group_size)

print(f"{group_size} companions received {math.floor(earn_money / group_size)} coins each.")
