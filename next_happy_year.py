year = int(input())

exist_digit =0
while exist_digit !=-1:
    distinct_digits = True
    text_year = str(year+1)
    for i in range(0, len(text_year)):
        digit = text_year[i]

        exist_digit = text_year.find(digit, i+1, len(text_year))

        if exist_digit !=-1:
            distinct_digits = False
            break

    if distinct_digits:
        print(text_year)
        break
    year+=1

