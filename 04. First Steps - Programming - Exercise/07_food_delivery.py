chicken_meal_count = int(input())
fish_meal_count = int(input())
vege_meal_count = int(input())
chicken_meal_price = 10.35
fish_meal_price = 12.40
vege_meal_price = 8.15
delivery_price = 2.50
total_chicken = chicken_meal_price * chicken_meal_count
total_fish = fish_meal_price * fish_meal_count
total_vege = vege_meal_price * vege_meal_count
all_meal = total_vege + total_fish + total_chicken
dessert = all_meal * 0.20
total_purchase = all_meal + dessert + delivery_price
print(total_purchase)
