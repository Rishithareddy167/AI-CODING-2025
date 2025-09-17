import random
import string
import time
from typing import List, Tuple

Student = Tuple[str, str, float]  # (Name, Roll No, CGPA)

def generate_students(n: int) -> List[Student]:
    students = []
    for i in range(n):
        name = ''.join(random.choices(string.ascii_uppercase, k=7))
        roll = f"SRU{1000+i}"
        cgpa = round(random.uniform(5.0, 10.0), 2)
        students.append((name, roll, cgpa))
    return students

# Quick Sort implementation
def quick_sort(arr: List[Student]) -> List[Student]:
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2][2]
    left = [x for x in arr if x[2] > pivot]
    middle = [x for x in arr if x[2] == pivot]
    right = [x for x in arr if x[2] < pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Merge Sort implementation
def merge_sort(arr: List[Student]) -> List[Student]:
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left: List[Student], right: List[Student]) -> List[Student]:
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i][2] > right[j][2]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def print_top_students(students: List[Student], top_n: int = 10):
    print(f"Top {top_n} Students by CGPA:")
    print(f"{'Name':<10} {'Roll No':<10} {'CGPA':<5}")
    for s in students[:top_n]:
        print(f"{s[0]:<10} {s[1]:<10} {s[2]:<5}")

def main():
    n = 10000  # Large dataset for performance comparison
    students = generate_students(n)

    # Quick Sort
    students_qs = students.copy()
    start_qs = time.time()
    sorted_qs = quick_sort(students_qs)
    end_qs = time.time()
    print(f"Quick Sort Time: {end_qs - start_qs:.6f} seconds")
    print_top_students(sorted_qs)

    # Merge Sort
    students_ms = students.copy()
    start_ms = time.time()
    sorted_ms = merge_sort(students_ms)
    end_ms = time.time()
    print(f"\nMerge Sort Time: {end_ms - start_ms:.6f} seconds")
    print_top_students(sorted_ms)

if __name__ == "__main__":
    main()