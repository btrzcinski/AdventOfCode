from collections import defaultdict
from operator import itemgetter

class Reindeer:
    def __init__(self, name, speed, flying_time, resting_time):
        self.name = name
        self.speed = speed
        self.flying_time = flying_time
        self.resting_time = resting_time

    def __repr__(self):
        return self.name

    def distance_traveled_by_time(self, t):
        period = self.flying_time + self.resting_time
        # how many total periods have elapsed in t?
        distance = (self.speed * self.flying_time) * (t // period)
        # how much time did we have left?
        remainder = t % period
        if remainder > self.flying_time: remainder = self.flying_time
        distance += (remainder * self.speed)
        return distance

def winning_reindeers_at_time(reindeer, t):
    distances = [(r, r.distance_traveled_by_time(t)) for r in reindeer]
    winner = max(distances, key=itemgetter(1))
    return [r for r in distances if r[1] == winner[1]]

def main():
    reindeer = []
    with open("Day14.txt") as f:
        for line in f:
            reindeer_name, _, _, speed, _, _, flying_time, _, _, _, _, _, _, resting_time, _ = line.split(" ")
            reindeer.append(Reindeer(reindeer_name, int(speed), int(flying_time), int(resting_time)))
    print("Distance winner at t = 2503:", winning_reindeers_at_time(reindeer, 2503))
    scores = defaultdict(int)
    for t in range(1, 2504):
        winners = winning_reindeers_at_time(reindeer, t)
        for winner in winners:
            scores[winner[0].name] += 1
    winner = max(scores, key=lambda k: scores[k])
    print("Points winner at t = 2503:", winner, ", points =", scores[winner])

if __name__ == "__main__":
    main()
