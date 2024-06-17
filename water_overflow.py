lines = int(input())
capacity =255
total_liters = 0
for i in range(lines):
    liters_of_water = int(input())

    if total_liters + liters_of_water > capacity:
        print("Insufficient capacity!")
    else:
        total_liters += liters_of_water

print(total_liters)