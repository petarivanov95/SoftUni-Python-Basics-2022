num_of_locations = int(input())

for location in range(num_of_locations):
    daily_planned_production = float(input())
    days_to_work = int(input())
    planned_production = daily_planned_production * days_to_work
    total_actual_production = 0
    for day in range(days_to_work):
        daily_actual_production = float(input())
        total_actual_production += daily_actual_production
    average_actual = total_actual_production / days_to_work

    if average_actual >= daily_planned_production:
        print(f"Good job! Average gold per day: {average_actual:.2f}.")
    else:
        difference = abs(average_actual - daily_planned_production)
        print(f"You need {difference:.2f} gold.")
