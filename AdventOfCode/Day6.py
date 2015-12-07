def turn_on_lights(lights, begin, end):
    for x in range(begin[0], end[0]+1):
        for y in range(begin[1], end[1]+1):
            lights[x][y] = True

def turn_off_lights(lights, begin, end):
    for x in range(begin[0], end[0]+1):
        for y in range(begin[1], end[1]+1):
            lights[x][y] = False

def toggle_lights(lights, begin, end):
    for x in range(begin[0], end[0]+1):
        for y in range(begin[1], end[1]+1):
            if lights[x][y]: lights[x][y] = False
            else: lights[x][y] = True

def coordinate_from_string(s):
    return tuple([int(x) for x in s.split(",")])

def lit_lights(lights):
    return sum(row.count(True) for row in lights)

def all_lights_off():
    return [([False] * 1000).copy() for x in range(0,1000)]

def main():
    lights = all_lights_off()
    with open("Day6.txt") as f:
        for command in [l.rstrip() for l in f.readlines()]:
            parts = command.split(" ")
            begin = coordinate_from_string(parts[-3])
            end = coordinate_from_string(parts[-1])
            if command.startswith("toggle"): toggle_lights(lights, begin, end)
            if parts[1] == "on": turn_on_lights(lights, begin, end)
            if parts[1] == "off": turn_off_lights(lights, begin, end)
    print("Lit lights: %d" % (lit_lights(lights),))

if __name__ == "__main__":
    main()