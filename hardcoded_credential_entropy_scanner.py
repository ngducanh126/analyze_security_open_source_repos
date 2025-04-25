def shannon_entropy(data):
    from math import log2
    if not data:
        return 0
    freq = {}
    for c in data:
        freq[c] = freq.get(c, 0) + 1
    entropy = 0
    for c in freq:
        p = freq[c] / len(data)
        entropy -= p * log2(p)
    return entropy

