number = int(input())
result=""
for i in range(number):
    for j in range(number):
        for k in range(number):
            result += chr(97 + i)
            result += chr(97 + j)
            result += chr(97 + k)
            print(result)
            result=""

