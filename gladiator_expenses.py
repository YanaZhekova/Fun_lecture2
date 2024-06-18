count_lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
shields_break = 0
swords_break = 0
armor_break = 0
helmet_break = 0
last_shield_break = 0
price_new_equipment = 0
for i in range(1, count_lost_fights + 1):
    if i % 2 == 0 and i % 3 != 0:
        helmet_break += 1
    elif i % 3 == 0 and i % 2 != 0:
        swords_break += 1
    elif i % 2 == 0 and i % 3 == 0:
        shields_break += 1
        helmet_break += 1
        swords_break += 1

    if shields_break % 2 == 0 and shields_break != 0 and last_shield_break != shields_break:
        last_shield_break = shields_break
        armor_break += 1

price_new_equipment = helmet_break * helmet_price + armor_break * armor_price + swords_break * sword_price + shields_break * shield_price

print(f"Gladiator expenses: {price_new_equipment:.2f} aureus")
