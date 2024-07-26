import random
from collections import defaultdict
from itertools import permutations

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

def generate_specific_random_triplets():
    numbers = [1, 3, 5]
    all_triplets = list(permutations(numbers))
    random.shuffle(all_triplets)
    
    written_triplets = []
    pair_counts = defaultdict(int)

    while all_triplets:
        new_triplet = all_triplets.pop()
        if written_triplets:
            last_pair = (written_triplets[-1][-1], new_triplet[0])
            pair_counts[last_pair] += 1

        for i in range(len(new_triplet) - 1):
            pair = (new_triplet[i], new_triplet[i + 1])
            pair_counts[pair] += 1
        
        written_triplets.append(new_triplet)
        
        # Check if all pairs are balanced
        counts = list(pair_counts.values())
        if max(counts) - min(counts) > 1:
            # If not balanced, revert the addition and shuffle
            for i in range(len(new_triplet) - 1):
                pair = (new_triplet[i], new_triplet[i + 1])
                pair_counts[pair] -= 1
            if written_triplets:
                last_pair = (written_triplets[-1][-1], new_triplet[0])
                pair_counts[last_pair] -= 1
            written_triplets.pop()
            random.shuffle(all_triplets)

    return written_triplets, pair_counts

def print_pair_counts(pair_counts):
    print("\nPair Counts:")
    for pair, count in pair_counts.items():
        print(f"{pair}: {count} times")

# Generate the triplets
written_triplets, pair_counts = generate_specific_random_triplets()

# Print the generated triplets
for triplet in written_triplets:
    print(triplet)

# Print the pair counts
print_pair_counts(pair_counts)