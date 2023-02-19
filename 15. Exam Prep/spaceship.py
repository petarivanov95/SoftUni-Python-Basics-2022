import math

ship_width = float(input())
ship_length = float(input())
ship_height = float(input())
average_height = float(input())

volume = ship_width * ship_length * ship_height
size_requirement = 2 * 2 * (average_height + 0.4)

num_astros = math.floor(volume / size_requirement)

if num_astros < 3:
    print(f"The spacecraft is too small.")
elif 3 <= num_astros <= 10:
    print(f"The spacecraft holds {num_astros} astronauts.")
else:
    print("The spacecraft is too big.")
