from operator import itemgetter

# graph: {'city': [('neighbor1', cost1), ('neighbor2', cost2)]}
def add_connection_to_graph(graph, start, end, cost):
    start_neighbors = graph.setdefault(start, [])
    if (end, cost) not in start_neighbors:
        start_neighbors.append((end, cost))
    end_neighbors = graph.setdefault(end, [])
    if (start, cost) not in end_neighbors:
        end_neighbors.append((start, cost))

def route_from_starting_city(graph, city, longest_path=False):
    cities_to_visit = list(graph.keys())
    paths = [([city], 0)]
    while len(paths[0][0]) != len(cities_to_visit):
        current_path, paths = paths[0], paths[1:]
        visited_cities, cost = current_path
        current_city = visited_cities[-1]
        for neighbor in graph[current_city]:
            neighbor_city, neighbor_cost = neighbor
            if neighbor_city not in visited_cities:
                new_path = (visited_cities.copy() + [neighbor_city], cost + neighbor_cost)
                paths.append(new_path)
        paths.sort(key=itemgetter(1), reverse=longest_path)
    return paths[0]

def route(graph, longest_path=False):
    paths = [route_from_starting_city(graph, c, longest_path) for c in graph]
    if longest_path:
        return max(paths, key=itemgetter(1))
    return min(paths, key=itemgetter(1))

def add_instruction_line_to_graph(graph, line):
    start, _, end, _, cost = line.split()
    add_connection_to_graph(graph, start, end, int(cost))

def main():
    graph = {}
    with open("Day9.txt") as f:
        for l in f.readlines():
            add_instruction_line_to_graph(graph, l.rstrip())
    print("Shortest: %s" % (repr(route(graph)),))
    print("Longest: %s" % (repr(route(graph, longest_path=True)),))

if __name__ == "__main__":
    main()
