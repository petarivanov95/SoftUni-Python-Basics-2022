sum_prime = 0
sum_others = 0

while True:
    current_input = input()
    if current_input == 'stop':
        print(f"Sum of all prime numbers is: {sum_prime}")
        print(f"Sum of all non prime numbers is: {sum_others}")
        break
    num_check = int(current_input)
    if num_check < 0:
        print('Number is negative.')
        num_check = 0
    is_prime = True
    if num_check == 0 or num_check == 1:
        sum_others += num_check
    for x in range(2, num_check):
        if num_check % x == 0:
            is_prime = False
            break

    if is_prime == True:
        sum_prime += num_check
    else:
        sum_others += num_check
