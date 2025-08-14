def recommend_books(books, preferred_genre):
    """
    Recommend books based on the user's preferred genre.

    Args:
        books (list of dict): List of books, each represented as a dictionary with 'title' and 'genre' keys.
        preferred_genre (str): The genre preferred by the user.

    Returns:
        list: List of book titles that match the preferred genre.
    """
    recommended = [book['title'] for book in books if book.get('genre', '').lower() == preferred_genre.lower()]
    return recommended

# Example usage
if __name__ == "__main__":
    books_list = [
        {'title': 'To Kill a Mockingbird', 'genre': 'Fiction'},
        {'title': 'A Brief History of Time', 'genre': 'Science'},
        {'title': 'The Great Gatsby', 'genre': 'Fiction'},
        {'title': 'The Art of Computer Programming', 'genre': 'Technology'},
        {'title': 'The Selfish Gene', 'genre': 'Science'},
    ]
    user_genre = input("Enter your preferred genre: ")
    recommendations = recommend_books(books_list, user_genre)
    if recommendations:
        print("Recommended books in the genre '{}':".format(user_genre))
        for title in recommendations:
            print("-", title)
    else:
        print("No books found in the genre '{}'.".format(user_genre))
