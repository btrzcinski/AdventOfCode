def total_delivered_houses(movedata, robosanta=True):
    presents_delivered = {}
    santa_location = {'santa': (0,0), 'robosanta': (0,0)}
    presents_delivered[(0, 0)] = 2

    current_santa = 'santa'
    for move in movedata:
        current_house = santa_location[current_santa]
        if move == '<':
            current_house = (current_house[0] - 1, current_house[1])
        elif move == '>':
            current_house = (current_house[0] + 1, current_house[1])
        elif move == '^':
            current_house = (current_house[0], current_house[1] - 1)
        elif move == 'v':
            current_house = (current_house[0], current_house[1] + 1)
        else:
            print("Warning: invalid move %s" % (move,))
            continue

        house_presents = presents_delivered.setdefault(current_house, 0)
        presents_delivered[current_house] = house_presents + 1

        santa_location[current_santa] = current_house
        if robosanta:
            if current_santa == 'santa': current_santa = 'robosanta'
            else: current_santa = 'santa'

    delivered_houses = len(presents_delivered)
    return delivered_houses

def get_movedata_from_file(filename):
    movedata = ""
    with open(sys.argv[1]) as f:
        movedata = f.read().rstrip()
    return movedata

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Give me an input file")
        exit()

    robosanta = True
    if len(sys.argv) > 2 and sys.argv[2] == 'norobo':
        robosanta = False

    delivered_houses = total_delivered_houses(get_movedata_from_file(sys.argv[1]), robosanta)

    print("Houses delivered to: %d" % (delivered_houses,))
