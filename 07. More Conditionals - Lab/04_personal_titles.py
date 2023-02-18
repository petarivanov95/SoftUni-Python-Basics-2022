age_input = int(input('age?' ))
gender_input = input('gender? ')

if gender_input == 'm':
    if age_input >= 16:
        print('Mr.')
    else:
        print("Master")
else:
    if age_input >= 16:
        print("Ms.")
    else:
        print("Miss")