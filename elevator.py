import math
number_of_people = int(input())
capacity = int(input())

if number_of_people % capacity == 0:
    courses = number_of_people / capacity
    print(f"{courses:.0f}")
elif number_of_people < capacity:
    print("1")

else:
    courses = number_of_people / capacity
    print(f"{math.ceil(courses):.0f}")

