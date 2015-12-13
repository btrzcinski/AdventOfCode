from itertools import permutations
from operator import itemgetter

class SeatingCalculator:
    def __init__(self, filename=None):
        self.reset()
        if filename is not None:
            self.set_happiness_map_from_file(filename)

    def set_happiness_value(self, guest, neighbor, units):
        guest_map = self.happiness_map.setdefault(guest, {})
        guest_map[neighbor] = units

    def add_guest_with_uniform_happiness(self, guest, units):
        for n in list(self.guest_list()):
            self.happiness_map[n][guest] = units
            self.happiness_map.setdefault(guest, {})[n] = units

    def reset(self):
        self.happiness_map = {}

    def set_happiness_map_from_file(self, filename):
        self.reset()
        with open(filename) as f:
            for l in f:
                parts = l.rstrip()[:-1].split(" ")
                guest = parts[0]
                sign = parts[2]
                units = int(parts[3])
                if sign == "lose":
                    units = -units
                neighbor = parts[-1]
                self.set_happiness_value(guest, neighbor, units)
    
    def guest_list(self):
        return self.happiness_map.keys()

    def calculate_arrangement_happiness(self, arrangement):
        # arrangement is a list that is circular, e.g.
        # [A, B, C, D] indicates a round table where A and D are
        # also next to each other
        total_happiness_change = 0
        for guest_n in range(len(arrangement)):
            left_neighbor = arrangement[guest_n - 1]
            if guest_n + 1 >= len(arrangement):
                right_neighbor = arrangement[0]
            else:
                right_neighbor = arrangement[guest_n + 1]
            guest = arrangement[guest_n]
            total_happiness_change += self.happiness_map[guest][left_neighbor]
            total_happiness_change += self.happiness_map[guest][right_neighbor]
        return total_happiness_change

    # returns: (total_happiness_change, [arrangement])
    def most_optimal_arrangement(self):
        scored_arrangements = []
        for arrangement_guests in permutations(self.guest_list()):
            scored_arrangements.append((self.calculate_arrangement_happiness(arrangement_guests), arrangement_guests))
        return max(scored_arrangements, key=itemgetter(0))

def main():
    calc = SeatingCalculator("Day13.txt")
    print("Optimal arrangement:", calc.most_optimal_arrangement())
    calc.add_guest_with_uniform_happiness("Barnett", 0)
    print("With neutral guest added:", calc.most_optimal_arrangement())

if __name__ == "__main__":
    main()