food_price = 12.45

num_cats = int(input())
small_cats = 0
medium_cats = 0
large_cats = 0
total_food = 0

for cat in range(num_cats):
    food_per_cat = float(input())
    if 100<= food_per_cat <200:
        small_cats += 1
        total_food += food_per_cat
    elif 200<= food_per_cat <300:
        medium_cats += 1
        total_food += food_per_cat
    elif 300<= food_per_cat < 400:
        large_cats += 1
        total_food += food_per_cat  

    
    food_cost = (total_food/1000)*food_price

print(f"Group 1: {small_cats} cats.")
print(f"Group 2: {medium_cats} cats.")
print(f"Group 3: {large_cats} cats.")
print(f"Price for food per day: {food_cost:.2f} lv.")
