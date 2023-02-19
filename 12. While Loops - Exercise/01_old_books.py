book_state = False
book_to_search = input()
searched_books = 0

while book_state == False:
    book_to_check = input()
    if book_to_check == book_to_search:
        book_state = True
        print(f"You checked {searched_books} books and found it.")

    if book_to_check == "No More Books":
        book_state = True
        print(f"The book you search is not here!")
        print(f"You checked {searched_books} books.")

    searched_books += 1
