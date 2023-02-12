pages = 899
covers = 2

price_print_page = float(input())
price_print_cover = float(input())
percent_reduction = int(input())
price_designer = float(input())
percent_team = int(input())

initial_cost = price_print_page*pages + price_print_cover*covers
cost = ((1-percent_reduction/100)*initial_cost + price_designer)*(1-percent_team/100)

print(f"Avtonom should pay {cost:.2f} BGN.")