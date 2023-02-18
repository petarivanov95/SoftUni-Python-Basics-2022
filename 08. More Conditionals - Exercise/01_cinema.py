movie_type = input()
rows = int(input())
cols = int(input())

if movie_type == 'Premiere':
    premiere_price = 12
    profits = rows*cols*premiere_price
    print(f'{profits:.2f}')
elif movie_type == 'Normal':
    premiere_price = 7.50
    profits = rows*cols*premiere_price 
    print(f'{profits:.2f}')
elif movie_type == 'Discount':
    premiere_price = 5.00
    profits = rows*cols*premiere_price 
    print(f'{profits:.2f}')