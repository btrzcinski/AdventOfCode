from itertools import combinations

def all_combinations_for_amount(containers, amount):
    result = []
    for n in range(len(containers)):
        result += [tuple(c) for c in combinations(containers, n) if sum(c) == amount]
    return result

def minimum_container_combinations(all_combinations):
    return [c for c in all_combinations if len(c) == len(min(all_combinations, key=len))]

def main():
    with open("Day17.txt") as f:
        containers = [int(l.strip()) for l in f]
    combinations = all_combinations_for_amount(containers, 150)
    print("Number of combinations that fit 150:", len(combinations))
    min_container_combinations = minimum_container_combinations(combinations)
    print("Number of combinations that fit 150 with min size (%d):" % len(min_container_combinations[0]), len(min_container_combinations))

if __name__ == "__main__":
    main()