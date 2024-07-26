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

def generate_specific_random_triplets(num_iterations=50):
    numbers = [1, 3, 5]
    written_triplets = []
    pair_counts = defaultdict(int)

    while len(written_triplets) < num_iterations:
        valid_triplet_found = False

        while not valid_triplet_found:
            new_triplet = get_random_triplets(numbers)
            if find_array(written_triplets, new_triplet):
                continue

            if len(written_triplets) > 0:
                last_pair = (written_triplets[-1][-2], written_triplets[-1][-1])
                new_pair = (new_triplet[0], new_triplet[1])
                if pair_counts[last_pair] != pair_counts[new_pair]:
                    continue

            if len(written_triplets) > 1:
                prev_pair = (written_triplets[-1][-1], new_triplet[0])
                if pair_counts[prev_pair] != pair_counts[(written_triplets[-2][-1], written_triplets[-1][0])]:
                    continue

            written_triplets.append(new_triplet)
            pair_counts[(new_triplet[0], new_triplet[1])] += 1
            valid_triplet_found = True
        
        print(new_triplet)
        if factorial(len(numbers)) == len(written_triplets):
            break

generate_specific_random_triplets()
