lily_age = int(input())
price_washer = float(input())
price_toy = int(input())
money_even_bday = 0
money_odd_bday = 0
past_evens = 0

for x in range(1, lily_age + 1):
    if x % 2 == 0:
        money_even_bday += (10 * past_evens) + 10
        past_evens += 1

    else:
        money_odd_bday += price_toy

total_money = money_even_bday + money_odd_bday - (past_evens * 1)
money_after = abs(total_money - price_washer)

if total_money >= price_washer:
    print(f"Yes! {money_after:.2f}")
else:
    print(f"No! {money_after:.2f}")
