steps_counter = 0
while True:
    current_steps = input()
    if current_steps != "Going home":
        steps_counter += int(current_steps)
        if steps_counter >= 10000:
            difference = abs(steps_counter - 10000)
            print("Goal reached! Good job!")
            print(f"{difference} steps over the goal!")
            break
    else:
        current_steps = input()
        steps_counter += int(current_steps)
        difference = abs(steps_counter - 10000)
        if steps_counter >= 10000:
            print("Goal reached! Good job!")
            print(f"{difference} steps over the goal!")
            break
        else:
            print(f"{difference} more steps to reach goal.")
            break
