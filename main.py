ˀimport random
from math import factorial

def get_random_triplets(numbers):
    new_triplet = numbers.copy()
    random.shuffle(new_triplet)
    return new_triplet

def find_array(lst, searched):
    for i in lst:
        if i == searched:
            return 1
    return 0

def generate_specific_random_triplets(num_iterations=6):
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

generate_specific_random_triplets()


