team = input()
souvenir_type = input()
num_souvenirs = int(input())
price = 0

teams = ["Argentina", "Brazil", "Croatia", "Denmark"]
souvenir_types = ["flags", "caps", "posters", "stickers"]

if team not in teams:
    print("Invalid country!")

if souvenir_type not in souvenir_types:
    print("Invalid stock!")

if team == "Argentina" and souvenir_type == "flags":
    price = 3.25
elif team == "Argentina" and souvenir_type == "caps":
    price = 7.20
elif team == "Argentina" and souvenir_type == "posters":
    price = 5.10
elif team == "Argentina" and souvenir_type == "stickers":
    price = 1.25
elif team == "Brazil" and souvenir_type == "flags":
    price = 4.20
elif team == "Brazil" and souvenir_type == "caps":
    price = 8.50
elif team == "Brazil" and souvenir_type == "posters":
    price = 5.35
elif team == "Brazil" and souvenir_type == "stickers":
    price = 1.20
elif team == "Croatia" and souvenir_type == "flags":
    price = 2.75
elif team == "Croatia" and souvenir_type == "caps":
    price = 6.90
elif team == "Croatia" and souvenir_type == "posters":
    price = 4.95
elif team == "Croatia" and souvenir_type == "stickers":
    price = 1.10
elif team == "Denmark" and souvenir_type == "flags":
    price = 3.10
elif team == "Denmark" and souvenir_type == "caps":
    price = 6.50
elif team == "Denmark" and souvenir_type == "posters":
    price = 4.80
elif team == "Denmark" and souvenir_type == "stickers":
    price = 0.90

cost = num_souvenirs * price
if cost != 0:
    print(f"Pepi bought {num_souvenirs} {souvenir_type} of {team} for {cost:.2f} lv.")
