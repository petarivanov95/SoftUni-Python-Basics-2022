city = input()
size_sales = float(input())
commission = None

if city == 'Sofia':
    if size_sales >= 0 and size_sales <= 500:
        commission = 0.05
    elif size_sales >= 500 and size_sales <= 1000:
        commission = 0.07 
    elif size_sales >= 1000 and size_sales <= 10000:
        commission = 0.08 
    elif size_sales >= 10000:
        commission = 0.12
    else:
        print('error') 
elif city == "Varna":
    if size_sales >= 0 and size_sales <= 500:
        commission = 0.045
    elif size_sales >= 500 and size_sales <= 1000:
        commission = 0.075 
    elif size_sales >= 1000 and size_sales <= 10000:
        commission = 0.10 
    elif size_sales >= 10000:
        commission = 0.13
    else:
        print('error')
elif city == "Plovdiv":
    if size_sales >= 0 and size_sales <= 500:
        commission = 0.055
    elif size_sales >= 500 and size_sales <= 1000:
        commission = 0.08 
    elif size_sales >= 1000 and size_sales <= 10000:
        commission = 0.12 
    elif size_sales >= 10000:
        commission = 0.145
    else:
        print('error')
else:
    print('error')

if commission != None:
    profit = commission*size_sales
    final_result = '{0:.2f}'.format(profit)
    print(final_result)