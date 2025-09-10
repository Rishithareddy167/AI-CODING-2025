def process_scores(scores):
    avg = sum(scores) / len(scores)
    highest = max(scores)
    lowest = min(scores)
    print("Average:", avg)
    print("Highest:", highest)
    print("Lowest:", lowest)

try:
    scores = list(map(float, input("Enter scores separated by commas: ").split(',')))
    process_scores(scores)
except Exception as e:
    print(f"Invalid input: {e}")