

import random
from collections import defaultdict
from itertools import permutations

def get_random_triplets(numbers):
    return list(permutations(numbers))

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

def is_valid_triplet(written_triplets, new_triplet):
    if written_triplets and written_triplets[-1] == new_triplet:
        return False
    if written_triplets and written_triplets[-1][-1] == new_triplet[0]:
        return False
    return True

def generate_specific_random_triplets(num_triplets=4):
    numbers = [1, 3, 5]
    all_triplets = get_random_triplets(numbers)
    written_triplets = []
    pair_counts = defaultdict(int)

    while len(written_triplets) < num_triplets:
        random.shuffle(all_triplets)
        for new_triplet in all_triplets:
            if not is_valid_triplet(written_triplets, new_triplet):
                continue
            
            temp_pair_counts = pair_counts.copy()
            for i in range(len(new_triplet) - 1):
                pair = (new_triplet[i], new_triplet[i + 1])
                temp_pair_counts[pair] += 1
            if written_triplets:
                last_pair = (written_triplets[-1][-1], new_triplet[0])
                temp_pair_counts[last_pair] += 1

            max_count = max(temp_pair_counts.values())
            min_count = min(temp_pair_counts.values())
            if max_count - min_count > 1:
                continue

            pair_counts = temp_pair_counts
            written_triplets.append(new_triplet)
            if len(written_triplets) >= num_triplets:
                break

    return written_triplets, pair_counts

def print_pair_counts(pair_counts):
    print("\nPair Counts:")
    for pair, count in pair_counts.items():
        print(f"{pair}: {count} times")

# Generate the triplets
written_triplets, pair_counts = generate_specific_random_triplets()

# Print the generated triplets
print("Generated Triplets:")
for triplet in written_triplets:
    print(triplet)

# Print the pair counts
print_pair_counts(pair_counts)
