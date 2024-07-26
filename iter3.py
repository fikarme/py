import random
from math import factorial
from collections import defaultdict

def get_random_triplets(numbers):
    new_triplet = numbers.copy()
    random.shuffle(new_triplet)
    return new_triplet

def find_array(lst, searched):
    for i in lst:
        if i == searched:
            return 1
    return 0

def count_adjacent_pairs(triplets):
    pair_counts = defaultdict(int)
    for i in range(len(triplets)):
        triplet = triplets[i]
        for j in range(len(triplet) - 1):
            pair = (triplet[j], triplet[j + 1])
            pair_counts[pair] += 1
        if i < len(triplets) - 1:
            next_triplet = triplets[i + 1]
            pair = (triplet[-1], next_triplet[0])
            pair_counts[pair] += 1
    return pair_counts

def generate_specific_random_triplets(num_iterations=12):
    numbers = [1, 3, 5]
    written_triplets = []

    for _ in range(num_iterations):
        while True:
            new_triplet = get_random_triplets(numbers)
            if find_array(written_triplets, new_triplet):
                continue
            if len(written_triplets) > 1 and written_triplets[-1][-1] == new_triplet[0]:
                continue
            written_triplets.append(new_triplet)
            break
        print(new_triplet)
        if factorial(len(numbers)) == len(written_triplets):
            break

    return written_triplets

def print_pair_counts(pair_counts):
    print("\nPair Counts:")
    for pair, count in pair_counts.items():
        print(f"{pair}: {count} times")

# Generate the triplets
written_triplets = generate_specific_random_triplets()

# Count the adjacent pairs
pair_counts = count_adjacent_pairs(written_triplets)

# Print the pair counts
print_pair_counts(pair_counts)
