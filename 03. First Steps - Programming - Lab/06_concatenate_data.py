first_name = input()
last_name = input()
age = int(input())
town = input()

# .format()
print(
    "You are {} {}, a {}-years old person from {}.".format(
        first_name, last_name, age, town
    )
)

# f-string
print(f"You are {first_name} {last_name}, a {age}-years old person from {town}.")
