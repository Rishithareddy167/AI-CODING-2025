import csv
import json
import time
from typing import List, Dict, Any

def load_books_csv(filename: str) -> List[Dict[str, Any]]:
    books = []
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            books.append(row)
    return books

def load_books_json(filename: str) -> List[Dict[str, Any]]:
    with open(filename, encoding='utf-8') as f:
        return json.load(f)

def linear_search(books: List[Dict[str, Any]], keyword: str) -> List[Dict[str, Any]]:
    keyword = keyword.lower()
    return [book for book in books if keyword in book['title'].lower() or keyword in book['author'].lower()]

def binary_search(books: List[Dict[str, Any]], keyword: str, key: str) -> List[Dict[str, Any]]:
    # Assumes books are sorted by the key (title or author)
    keyword = keyword.lower()
    left, right = 0, len(books) - 1
    results = []
    while left <= right:
        mid = (left + right) // 2
        value = books[mid][key].lower()
        if keyword == value:
            # Find all matches (could be multiple)
            l, r = mid, mid
            while l >= 0 and books[l][key].lower() == keyword:
                l -= 1
            while r < len(books) and books[r][key].lower() == keyword:
                r += 1
            results.extend(books[l+1:r])
            break
        elif keyword < value:
            right = mid - 1
        else:
            left = mid + 1
    return results

def build_hash_table(books: List[Dict[str, Any]], key: str) -> Dict[str, List[Dict[str, Any]]]:
    table = {}
    for book in books:
        k = book[key].lower()
        if k not in table:
            table[k] = []
        table[k].append(book)
    return table

def hash_search(table: Dict[str, List[Dict[str, Any]]], keyword: str) -> List[Dict[str, Any]]:
    return table.get(keyword.lower(), [])

def compare_searches(books: List[Dict[str, Any]], keyword: str):
    print(f"Searching for: {keyword}\n")

    # Linear Search
    start = time.time()
    linear_results = linear_search(books, keyword)
    end = time.time()
    print(f"Linear Search: {len(linear_results)} result(s) in {end - start:.6f} seconds")

    # Binary Search (by title)
    books_by_title = sorted(books, key=lambda x: x['title'].lower())
    start = time.time()
    binary_results = binary_search(books_by_title, keyword, 'title')
    end = time.time()
    print(f"Binary Search (title): {len(binary_results)} result(s) in {end - start:.6f} seconds")

    # Hash-based Search (by title)
    hash_table = build_hash_table(books, 'title')
    start = time.time()
    hash_results = hash_search(hash_table, keyword)
    end = time.time()
    print(f"Hash Search (title): {len(hash_results)} result(s) in {end - start:.6f} seconds")

    # Show results (first 5)
    if linear_results:
        print("\nSample Results:")
        for book in linear_results[:5]:
            print(f"Title: {book['title']}, Author: {book['author']}")
    else:
        print("No results found.")

def main():
    # Example: load from CSV or JSON (uncomment as needed)
    # books = load_books_csv('books.csv')
    # books = load_books_json('books.json')

    # For demonstration, create a sample dataset
    books = [
        {'title': 'Data Science Handbook', 'author': 'Jake VanderPlas'},
        {'title': 'Python Crash Course', 'author': 'Eric Matthes'},
        {'title': 'Deep Learning', 'author': 'Ian Goodfellow'},
        {'title': 'Artificial Intelligence', 'author': 'Stuart Russell'},
        {'title': 'Pattern Recognition', 'author': 'Christopher Bishop'},
        {'title': 'Machine Learning', 'author': 'Tom Mitchell'},
        {'title': 'Introduction to Algorithms', 'author': 'Thomas H. Cormen'},
        {'title': 'Clean Code', 'author': 'Robert C. Martin'},
        {'title': 'The Pragmatic Programmer', 'author': 'Andrew Hunt'},
        {'title': 'Fluent Python', 'author': 'Luciano Ramalho'},
    ]

    keyword = input("Enter a keyword (title or author): ")
    compare_searches(books, keyword)

if __name__ == "__main__":
    main()