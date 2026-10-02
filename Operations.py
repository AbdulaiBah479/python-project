# Data structures (global for simplicity)
books = {}  # Dictionary: ISBN -> {"title": str, "author": str, "genre": str, "total_copies": int}
members = []  # List of dicts: {"member_id": int, "name": str, "email": str, "borrowed_books": list of ISBNs}
genres = ("Fiction", "Non-Fiction", "Sci-Fi")  # Tuple of valid genres

# 1. Add a book
def add_book(isbn, title, author, genre, total_copies):
    if isbn in books:
        print("Error: Book with this ISBN already exists.")
        return
    if genre not in genres:
        print("Error: Invalid genre. Must be one of:", genres)
        return
    books[isbn] = {
        "title": title,
        "author": author,
        "genre": genre,
        "total_copies": total_copies
    }
    print("Book added successfully.")

# 2. Add a member
def add_member(member_id, name, email):
    for member in members:
        if member["member_id"] == member_id:
            print("Error: Member with this ID already exists.")
            return
    members.append({
        "member_id": member_id,
        "name": name,
        "email": email,
        "borrowed_books": []
    })
    print("Member added successfully.")

# 3. Search book (by title or author)
def search_book(query):
    results = []
    for isbn, book in books.items():
        if query.lower() in book["title"].lower() or query.lower() in book["author"].lower():
            results.append((isbn, book))
    if results:
        for isbn, book in results:
            print(f"ISBN: {isbn}, Title: {book['title']}, Author: {book['author']}, Genre: {book['genre']}, Copies: {book['total_copies']}")
    else:
        print("No books found.")

# 4. Update book details
def update_book(isbn, title=None, author=None, genre=None, total_copies=None):
    if isbn not in books:
        print("Error: Book not found.")
        return
    if title:
        books[isbn]["title"] = title
    if author:
        books[isbn]["author"] = author
    if genre:
        if genre not in genres:
            print("Error: Invalid genre.")
            return
        books[isbn]["genre"] = genre
    if total_copies is not None:
        books[isbn]["total_copies"] = total_copies
    print("Book updated successfully.")

# 5. Delete book (only if not borrowed)
def delete_book(isbn):
    if isbn not in books:
        print("Error: Book not found.")
        return
    for member in members:
        if isbn in member["borrowed_books"]:
            print("Error: Cannot delete, book is borrowed.")
            return
    del books[isbn]
    print("Book deleted successfully.")

# 6. Borrow book
def borrow_book(member_id, isbn):
    # Find member
    member = next((m for m in members if m["member_id"] == member_id), None)
    if not member:
        print("Error: Member not found.")
        return
    if len(member["borrowed_books"]) >= 3:
        print("Error: Member has reached borrow limit (3 books).")
        return
    if isbn not in books:
        print("Error: Book not found.")
        return
    if books[isbn]["total_copies"] <= 0:
        print("Error: No copies available.")
        return
    # Borrow it
    member["borrowed_books"].append(isbn)
    books[isbn]["total_copies"] -= 1
    print("Book borrowed successfully.")

# 7. Return book
def return_book(member_id, isbn):
    # Find member
    member = next((m for m in members if m["member_id"] == member_id), None)
    if not member:
        print("Error: Member not found.")
        return
    if isbn not in member["borrowed_books"]:
        print("Error: Member did not borrow this book.")
        return
    if isbn not in books:
        print("Error: Book not found.")  # Shouldn't happen, but check
        return
    # Return it
    member["borrowed_books"].remove(isbn)
    books[isbn]["total_copies"] += 1
    print("Book returned successfully.")


