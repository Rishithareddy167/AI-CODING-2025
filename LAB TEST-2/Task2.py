def check_membership(corpus, stream):
    corpus_set = set(corpus)
    return [item in corpus_set for item in stream]

# Example usage
corpus = [1, 2, 3, 4, 5]
stream = [2, 5, 9]
result = check_membership(corpus, stream)
print(result)  # Output: [True, True, False]

# Complexity improvement:
# - Converting corpus to set: O(n)
# - Each lookup: O(1) average, so total O(m) for m items in stream
# - Total: O(n + m), much faster than O(n*m) for list membership

# Micro-bench ideas:
# - Compare timing of set vs list membership for large corpus/stream
# - Profile memory usage for very large corpus