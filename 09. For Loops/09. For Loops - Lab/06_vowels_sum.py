a = 1
e = 2
i = 3
o = 4
u = 5

my_string = input()
my_sum = 0

for x in my_string:
    if x == 'a':
        my_sum += a
    elif x == 'e':
        my_sum += e
    elif x == 'i':
        my_sum += i
    elif x == 'o':
        my_sum += o
    elif x == 'u':
        my_sum += u
    else:
        pass

print(my_sum)