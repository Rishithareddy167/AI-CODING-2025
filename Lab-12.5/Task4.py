import random
import string
import time
from typing import List, Dict

class Stock:
    def __init__(self, symbol: str, open_price: float, close_price: float):
        self.symbol = symbol
        self.open_price = open_price
        self.close_price = close_price
        self.pct_change = ((close_price - open_price) / open_price) * 100

    def __repr__(self):
        return f"{self.symbol}: Open={self.open_price:.2f}, Close={self.close_price:.2f}, Change={self.pct_change:.2f}%"

def simulate_stocks(n: int) -> List[Stock]:
    stocks = []
    for _ in range(n):
        symbol = ''.join(random.choices(string.ascii_uppercase, k=4))
        open_price = round(random.uniform(10, 500), 2)
        close_price = round(open_price * random.uniform(0.95, 1.05), 2)
        stocks.append(Stock(symbol, open_price, close_price))
    return stocks

# Heap Sort implementation
def heapify(arr: List[Stock], n: int, i: int):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[l].pct_change > arr[largest].pct_change:
        largest = l
    if r < n and arr[r].pct_change > arr[largest].pct_change:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr: List[Stock]):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    arr.reverse()  # For descending order

# Hash Map search
def build_stock_map(stocks: List[Stock]) -> Dict[str, Stock]:
    return {stock.symbol: stock for stock in stocks}

def search_stock(stock_map: Dict[str, Stock], symbol: str) -> Stock:
    return stock_map.get(symbol)

def main():
    n = 10000  # Number of stocks
    stocks = simulate_stocks(n)

    # Heap Sort
    stocks_hs = stocks.copy()
    start = time.time()
    heap_sort(stocks_hs)
    end = time.time()
    print(f"Heap Sort Time: {end - start:.6f} seconds")
    print("Top 5 Stocks by Gain/Loss (Heap Sort):")
    for s in stocks_hs[:5]:
        print(s)

    # Standard sorted()
    start = time.time()
    stocks_sorted = sorted(stocks, key=lambda s: s.pct_change, reverse=True)
    end = time.time()
    print(f"\nStandard sorted() Time: {end - start:.6f} seconds")
    print("Top 5 Stocks by Gain/Loss (sorted()):")
    for s in stocks_sorted[:5]:
        print(s)

    # Build Hash Map
    stock_map = build_stock_map(stocks)

    # Hash Map Search
    test_symbol = stocks[0].symbol
    start = time.time()
    result = search_stock(stock_map, test_symbol)
    end = time.time()
    print(f"\nHash Map Search Time: {end - start:.8f} seconds for symbol {test_symbol}")
    print(f"Result: {result}")

    # Standard dict lookup
    stock_dict = {s.symbol: s for s in stocks}
    start = time.time()
    result2 = stock_dict.get(test_symbol)
    end = time.time()
    print(f"Standard dict lookup Time: {end - start:.8f} seconds for symbol {test_symbol}")
    print(f"Result: {result2}")

    print("\nTrade-offs:")
    print("- Heap Sort is efficient for in-place sorting, but Python's built-in sorted() is highly optimized.")
    print("- Hash Map (dict) provides O(1) average-case search, ideal for instant lookups.")

if __name__ == "__main__":
    main()