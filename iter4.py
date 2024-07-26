import random
from collections import defaultdict

def get_random_triplets(numbers):
    new_triplet = numbers.copy()
    random.shuffle(new_triplet)
    return new_triplet

def find_array(lst, searched):
    for i in lst:
        if i == searched:
            return True
    return False

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
    pair_counts = defaultdict(int)

    for _ in range(num_iterations):
        valid_triplet_found = False

        while not valid_triplet_found:
            new_triplet = get_random_triplets(numbers)
            if find_array(written_triplets, new_triplet):
                continue
            

            # Accept the new triplet
            for i in range(len(new_triplet) - 1):
                pair = (new_triplet[i], new_triplet[i + 1])
                pair_counts[pair] += 1
            if len(written_triplets) > 0:
                last_pair = (written_triplets[-1][-1], new_triplet[0])
                pair_counts[last_pair] += 1

            written_triplets.append(new_triplet)
            valid_triplet_found = True
            # Ensure pair balance
            temp_pair_counts = pair_counts.copy()
            for i in range(len(new_triplet) - 1):
                pair = (new_triplet[i], new_triplet[i + 1])
                temp_pair_counts[pair] += 1
            if len(written_triplets) > 0:
                last_pair = (written_triplets[-1][-1], new_triplet[0])
                temp_pair_counts[last_pair] += 1

            # Check if the pair counts are still balanced
            max_count = max(temp_pair_counts.values())
            min_count = min(temp_pair_counts.values())
            if max_count - min_count > 1:
                continue
        
        print(new_triplet)
        if max(pair_counts.values()) == min(pair_counts.values()):
            break

    return written_triplets, pair_counts

def print_pair_counts(pair_counts):
    print("\nPair Counts:")
    for pair, count in pair_counts.items():
        print(f"{pair}: {count} times")

# Generate the triplets
written_triplets, pair_counts = generate_specific_random_triplets()

# Print the pair counts
print_pair_counts(pair_counts)
