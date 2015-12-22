class Lightboard:
    def __init__(self, size):
        self.board = [[0 for x in range(size)] for x in range(size)]
        self.size = size

    def __repr__(self):
        light_mapping = {0: '.', 1: '#'}
        return "\n".join(["".join([light_mapping[light] for light in row]) for row in self.board])

    def __getitem__(self, key):
        row, col = key
        if row < 0 or row >= self.size: return 0
        if col < 0 or col >= self.size: return 0
        return self.board[row][col]

    def __setitem__(self, key, value):
        row, col = key
        if row < 0 or row >= self.size: return
        if col < 0 or col >= self.size: return
        self.board[row][col] = value

    def neighbors_on_for_light(self, key):
        row, col = key
        return sum([sum([self[r,c] for c in range(col-1,col+2)]) for r in range(row-1,row+2)]) - self[row,col]

    def iterate(self, n=1, corners_always_on=False):
        corners = [(0,0), (0, self.size-1), (self.size-1, 0), (self.size-1, self.size-1)]
        if corners_always_on:
            for c in corners:
                self[c] = 1
        positions = []
        for r in range(self.size):
            for c in range(self.size):
                if not corners_always_on or (r,c) not in corners:
                    positions.append((r,c))
        for _ in range(n):
            lights_on = [p for p in positions if self[p] == 1]
            lights_off = [p for p in positions if self[p] == 0]
            lights_to_turn_off = [p for p in lights_on if self.neighbors_on_for_light(p) not in (2, 3)]
            lights_to_turn_on = [p for p in lights_off if self.neighbors_on_for_light(p) == 3]
            for l in lights_to_turn_off: self[l] = 0
            for l in lights_to_turn_on: self[l] = 1

    def number_of_lights_on(self):
        return sum([sum([self[r,c] for c in range(self.size)]) for r in range(self.size)])

def main():
    board = Lightboard(100)
    board2 = Lightboard(100)
    with open("Day18.txt") as f:
        row = 0
        for l in f:
            lights = l.strip()
            for col in range(100):
                if lights[col] == "#":
                    board[row,col] = 1
                    board2[row,col] = 1
            row += 1
    board.iterate(100)
    print("Number of lights on:", board.number_of_lights_on())
    board2.iterate(n=100, corners_always_on=True)
    print("Number of lights on with corners always on:", board2.number_of_lights_on())

if __name__ == "__main__":
    main()
