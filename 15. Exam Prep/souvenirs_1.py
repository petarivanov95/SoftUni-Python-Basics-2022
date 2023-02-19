team = input()
souvenir_type = input()
num_souvenirs = int(input())
price = 0

if team == "Argentina":
    if souvenir_type == "flags":
        price = 3.25
    elif souvenir_type == "caps":
        price = 7.20
    elif souvenir_type == "posters":
        price = 5.10
    elif souvenir_type == "stickers":
        price = 1.25
elif team == "Brazil":
    if souvenir_type == "flags":
        price = 4.20
    elif souvenir_type == "caps":
        price = 8.50
    elif souvenir_type == "posters":
        price = 5.35
    elif souvenir_type == "stickers":
        price = 1.20
elif team == "Croatia":
    if souvenir_type == "flags":
        price = 2.75
    elif souvenir_type == "caps":
        price = 6.90
    elif souvenir_type == "posters":
        price = 4.95
    elif souvenir_type == "stickers":
        price = 1.10
elif team == "Denmark":
    if souvenir_type == "flags":
        price = 3.10
    elif souvenir_type == "caps":
        price = 6.50
    elif souvenir_type == "posters":
        price = 4.80
    elif souvenir_type == "stickers":
        price = 0.90
cost = num_souvenirs * price
if cost != 0:
    print(f"Pepi bought {num_souvenirs} {souvenir_type} of {team} for {cost:.2f} lv.")

if team != "Argentina":
    print("Invalid country!")
elif team != "Brazil":
    print("Invalid country!")
elif team != "Croatia":
    print("Invalid country!")
elif team != "Denmark":
    print("Invalid country!")

if souvenir_type != "flags":
    print("Invalid stock!")
elif souvenir_type != "caps":
    print("Invalid stock!")
elif souvenir_type != "posters":
    print("Invalid stock!")
elif souvenir_type != "stickers":
    print("Invalid stock!")
