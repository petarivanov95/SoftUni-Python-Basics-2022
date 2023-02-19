n = int(input())

# thousands
for dig1 in range(1, 9 + 1):
    # hundreds
    for dig2 in range(1, 9 + 1):
        # tens
        for dig3 in range(1, 9 + 1):
            # ones
            for dig4 in range(1, 9 + 1):
                is_special = (
                    n % dig1 == 0 and n % dig2 == 0 and n % dig3 == 0 and n % dig4 == 0
                )

                if is_special:
                    print(f"{dig1}{dig2}{dig3}{dig4}", end=" ")
