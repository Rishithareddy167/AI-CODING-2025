def compute_ratios(values):
    results = []
    for i in range(len(values)):
        for j in range(i + 1, len(values)):  # Start from i+1 to avoid division by zero
            if values[j] != values[i]:  # Check for division by zero
                ratio = values[i] / (values[j] - values[i])
                results.append((i, j, ratio))
    return results

values = [5, 10, 15, 20, 25]
print(compute_ratios(values))