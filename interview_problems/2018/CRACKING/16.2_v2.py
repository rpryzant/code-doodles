from collections import Counter


def count_freqs(book, prev_counts=None):
    counts = Counter(book.split())

    # merge
    if prev_counts is not None:
        for k, v in prev_counts:
            counts[k] += v

    return counts

