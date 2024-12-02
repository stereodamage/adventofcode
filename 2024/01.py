from collections import Counter

def split_input(text):
    l1, l2 = zip(*(map(int, line.split("   ")) for line in text.strip().split("\n")))
    return list(l1), list(l2)

# day one, part one
def find_distance_in_input(list1, list2):
    return sum(abs(a - b) for a, b in zip(sorted(list1), sorted(list2)))

# day one, part two
def find_similarity_score(list1, list2):
    count_map = Counter(list2)
    return sum(a * count_map[a] for a in sorted(list1))