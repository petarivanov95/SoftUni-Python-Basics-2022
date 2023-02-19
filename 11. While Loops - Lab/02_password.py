username = input()
password = input()

input_for_pass = input()

while input_for_pass != password:
    input_for_pass = input()

print(f"Welcome {username}!")
