fruit = input()
day = input()
qty = float(input())
working_days = ["Monday","Tuesday",'Wednesday','Thursday','Friday']
weekend = ['Saturday','Sunday']
my_price = 0

if fruit == 'banana' and day in working_days:
    my_price = 2.50
    actual_price = qty*my_price
    final_result = '{0:.2f}'.format(actual_price)
    print(final_result)
elif fruit == 'apple' and day in working_days:
    my_price = 1.20
    actual_price = qty*my_price
    final_result = '{0:.2f}'.format(actual_price)
    print(final_result)
elif fruit == 'orange' and day in working_days:
    my_price = 0.85
    actual_price = qty*my_price
    final_result = '{0:.2f}'.format(actual_price)
    print(final_result)
elif fruit == 'grapefruit' and day in working_days:
    my_price = 1.45
    actual_price = qty*my_price
    final_result = '{0:.2f}'.format(actual_price)
    print(final_result)
elif fruit == 'kiwi' and day in working_days:
    my_price = 2.70
    actual_price = qty*my_price
    final_result = '{0:.2f}'.format(actual_price)
    print(final_result)
elif fruit == 'pineapple' and day in working_days:
    my_price = 5.50
    actual_price = qty*my_price
    final_result = '{0:.2f}'.format(actual_price)
    print(final_result)
elif fruit == 'grapes' and day in working_days:
    my_price = 3.85
    actual_price = qty*my_price
    final_result = '{0:.2f}'.format(actual_price)
    print(final_result)
elif fruit == 'banana' and day in weekend:
    my_price = 2.70
    actual_price = qty*my_price
    final_result = '{0:.2f}'.format(actual_price)
    print(final_result)
elif fruit == 'apple' and day in weekend:
    my_price = 1.25
    actual_price = qty*my_price
    final_result = '{0:.2f}'.format(actual_price)
    print(final_result)
elif fruit == 'orange' and day in weekend:
    my_price = 0.90
    actual_price = qty*my_price
    final_result = '{0:.2f}'.format(actual_price)
    print(final_result)
elif fruit == 'grapefruit' and day in weekend:
    my_price = 1.60
    actual_price = qty*my_price
    final_result = '{0:.2f}'.format(actual_price)
    print(final_result)
elif fruit == 'kiwi' and day in weekend:
    my_price = 3.00
    actual_price = qty*my_price
    final_result = '{0:.2f}'.format(actual_price)
    print(final_result)
elif fruit == 'pineapple' and day in weekend:
    my_price = 5.60
    actual_price = qty*my_price
    final_result = '{0:.2f}'.format(actual_price)
    print(final_result)
elif fruit == 'grapes' and day in weekend:
    my_price = 4.20
    actual_price = qty*my_price
    final_result = '{0:.2f}'.format(actual_price)
    print(final_result)
else:
    print("error")