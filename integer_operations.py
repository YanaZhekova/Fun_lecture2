import math
first_num = int(input())
second_num = int(input())
third_num = int(input())
fourth_num = int(input())

sum = first_num + second_num
result = (math.floor(sum / third_num)) * fourth_num

print(f"{result:.0f}")
