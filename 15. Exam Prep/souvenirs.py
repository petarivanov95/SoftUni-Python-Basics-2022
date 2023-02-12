team = input()
souvenir_type = input()
num_souvenirs = int(input())
teams = ['Argentina','Brazil','Croatia','Denmark']
souvenir_types = ['flags','caps','posters','stickers']

if team not in teams:
    print("Invalid country!")

if souvenir_type not in souvenir_types:
    print('Invalid stock')
# if team != 'Argentina' or team != 'Brazil' or team != 'Croatia' or team != 'Denmark':
#     print("Invalid country!")
# if souvenir_type != 'flags' or souvenir_type != 'caps' or souvenir_type != 'posters' or souvenir_type != 'stickers':
#     print('Invalid stock')

if team == 'Argentina' and souvenir_type == 'flags':
    price = 3.25
    cost = num_souvenirs*price
elif team == 'Argentina' and souvenir_type == 'caps':
    price = 7.20
    cost = num_souvenirs*price
elif team == 'Argentina' and souvenir_type == 'posters':
    price = 5.10
    cost = num_souvenirs*price
elif team == 'Argentina' and souvenir_type == 'stickers':
    price = 1.25
    cost = num_souvenirs*price

elif team == 'Brazil' and souvenir_type == 'flags':
    price = 4.20
    cost = num_souvenirs*price
elif team == 'Brazil' and souvenir_type == 'caps':
    price = 8.50
    cost = num_souvenirs*price
elif team == 'Brazil' and souvenir_type == 'posters':
    price = 5.35
    cost = num_souvenirs*price
elif team == 'Brazil' and souvenir_type == 'stickers':
    price = 1.20
    cost = num_souvenirs*price

elif team == 'Croatia' and souvenir_type == 'flags':
    price = 2.75
    cost = num_souvenirs*price
elif team == 'Croatia' and souvenir_type == 'caps':
    price = 6.90
    cost = num_souvenirs*price
elif team == 'Croatia' and souvenir_type == 'posters':
    price = 4.95
    cost = num_souvenirs*price
elif team == 'Croatia' and souvenir_type == 'stickers':
    price = 1.10
    cost = num_souvenirs*price

elif team == 'Denmark' and souvenir_type == 'flags':
    price = 3.10
    cost = num_souvenirs*price
elif team == 'Denmark' and souvenir_type == 'caps':
    price = 6.50
    cost = num_souvenirs*price
elif team == 'Denmark' and souvenir_type == 'posters':
    price = 4.80
    cost = num_souvenirs*price
elif team == 'Denmark' and souvenir_type == 'stickers':
    price = 0.90
    cost = num_souvenirs*price

print(f'Pepi bought {num_souvenirs} {souvenir_type} of {team} for {cost:.2f} lv.')