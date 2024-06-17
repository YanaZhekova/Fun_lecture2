number = int(input())

for i in range(1, number + 1):
    sum = 0
    if i >= 10:
        num = i
        while num > 0:
            current_number = num % 10
            sum += current_number
            num = (num - current_number) / 10

    else:
        sum += i
    if sum == 5 or sum == 7 or sum == 11:
        print(f"{i} -> True")
    else:
        print(f"{i} -> False")
