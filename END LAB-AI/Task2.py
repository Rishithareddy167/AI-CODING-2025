"""
Warehouse Search Tool
---------------------
Implements:
    1. Linear Search
    2. Binary Search

Both functions return:
    - index (if found)
    - comparison count
"""

# ---------------------------
# Linear Search
# ---------------------------
def linear_search(arr, target):
    """
    Performs Linear Search.
    Returns (index, comparisons)
    """
    comparisons = 0

    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == target:
            return i, comparisons

    return -1, comparisons  # Not found


# ---------------------------
# Binary Search
# ---------------------------
def binary_search(arr, target):
    """
    Performs Binary Search on a sorted list.
    Returns (index, comparisons)
    """
    low = 0
    high = len(arr) - 1
    comparisons = 0

    while low <= high:
        comparisons += 1
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid, comparisons
        elif target < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1, comparisons  # Not found


# -------------------------------------------------------
# TEST CASES (AI-Assisted Output)
# -------------------------------------------------------
warehouse_items = [5, 12, 19, 23, 34, 45, 56, 67, 72, 88]
target = 34

print("Warehouse Inventory:", warehouse_items)
print("Searching for item:", target)
print("\n----- Linear Search -----")
lin_index, lin_comp = linear_search(warehouse_items, target)
print("Found at index :", lin_index)
print("Comparisons    :", lin_comp)

print("\n----- Binary Search -----")
bin_index, bin_comp = binary_search(warehouse_items, target)
print("Found at index :", bin_index)
print("Comparisons    :", bin_comp)
