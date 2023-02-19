price_toy = 5
price_sweater = 15
kids = 0
adults = 0

while True:
    persons_input = input()
    if persons_input != "Christmas":
        persons_age = int(persons_input)
        if int(persons_input) <= 16:
            kids += 1
        else:
            adults += 1
    else:
        break


cost_toys = price_toy * kids
cost_sweaters = price_sweater * adults

print(f"Number of adults: {adults}")
print(f"Number of kids: {kids}")
print(f"Money for toys: {cost_toys:.0f}")
print(f"Money for sweaters: {cost_sweaters:.0f}")
