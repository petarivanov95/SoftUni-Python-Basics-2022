degrees = int(input())
time = input()
outfit = None
shoes = None

if 10 <= degrees <= 18 and time == "Morning":
    outfit = "Sweatshirt"
    shoes = "Sneakers"
elif 18 < degrees <= 24 and time == "Morning":
    outfit = "Shirt"
    shoes = "Moccasins"
elif 24 < degrees and time == "Morning":
    outfit = "T-Shirt"
    shoes = "Sandals"
elif 10 <= degrees <= 18 and time == "Afternoon":
    outfit = "Shirt"
    shoes = "Moccasins"
elif 18 < degrees <= 24 and time == "Afternoon":
    outfit = "T-Shirt"
    shoes = "Sandals"
elif 24 < degrees and time == "Afternoon":
    outfit = "Swim Suit"
    shoes = "Barefoot"
elif 10 <= degrees <= 18 and time == "Evening":
    outfit = "Shirt"
    shoes = "Moccasins"
elif 18 < degrees <= 24 and time == "Evening":
    outfit = "Shirt"
    shoes = "Moccasins"
elif 24 < degrees and time == "Evening":
    outfit = "Shirt"
    shoes = "Moccasins"


print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
