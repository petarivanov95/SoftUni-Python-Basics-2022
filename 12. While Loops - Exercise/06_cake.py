side1 = int(input())
side2 = int(input())

area = side1 * side2
pieces_taken = 0
while True:
    pieces = input()
    if pieces == "STOP":

        print(f"{abs(area)} pieces are left.")
        break
    else:
        pieces_taken = int(pieces)
        area -= pieces_taken
        if area <= 0:
            print(f"No more cake left! You need {abs(area)} pieces more.")
            break
