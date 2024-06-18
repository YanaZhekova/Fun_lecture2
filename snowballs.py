number_of_snowballs = int(input())
highest_snowball = 0
highest_snowball_weight=0
highest_snowball_time=0
highest_snowball_quality=0
for i in range(1, number_of_snowballs + 1):
    weight_snowball = int(input())
    time = int(input())
    quality = int(input())

    value = (weight_snowball / time) ** quality
    if i == 1:
        highest_snowball = value
        highest_snowball_weight = weight_snowball
        highest_snowball_time = time
        highest_snowball_quality = quality
    if value > highest_snowball:
        highest_snowball = value
        highest_snowball_weight = weight_snowball
        highest_snowball_time = time
        highest_snowball_quality = quality

print(f"{highest_snowball_weight} : {highest_snowball_time} = {highest_snowball:.0f} ({highest_snowball_quality})")