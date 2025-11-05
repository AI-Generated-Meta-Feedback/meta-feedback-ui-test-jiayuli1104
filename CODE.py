FUNCTION sortBooks(bookList):
    # bookList is a list of books
    # each book has: shelfNumber, returnOrder

    FOR i FROM 1 TO length(bookList) - 1:
        keyBook = bookList[i]
        j = i - 1

        # Compare keyBook with books before it
        WHILE j >= 0 AND compare(keyBook, bookList[j]) IS TRUE:
            bookList[j + 1] = bookList[j]     # shift right
            j = j - 1

        bookList[j + 1] = keyBook             # insert keyBook into position

    RETURN bookList


FUNCTION compare(bookA, bookB):
    # Return TRUE if bookA should come before bookB

    IF bookA.shelfNumber < bookB.shelfNumber:
        RETURN TRUE

    ELSE IF bookA.shelfNumber == bookB.shelfNumber:
        IF bookA.returnOrder < bookB.returnOrder:
            RETURN TRUE

    RETURN FALSE


