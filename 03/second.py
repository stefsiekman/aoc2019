import aoc.input
import first


def list_intersections(visited):
    return set(pos for pos in visited[0] if pos in visited[1])


def dist_to_intersections(intersections, wire):
    distances = dict()
    position = (0, 0)
    steps = 0

    for movement in wire:
        delta = first.dirs[movement[0]]
        amount = int(movement[1:])
        for _ in range(amount):
            position = (position[0] + delta[0], position[1] + delta[1])
            steps += 1
            if position in intersections:
                distances[position] = steps

    return distances


def min_total_distance(distances):
    return min(distances[0][pos] + distances[1][pos] for pos in distances[1])


def solve(wires):
    wire_nodes = [first.nodes(w) for w in wires]
    intersections = list_intersections(wire_nodes)
    distances = [dist_to_intersections(intersections, wire) for wire in wires]
    return min_total_distance(distances)


if __name__ == "__main__":
    lines = aoc.input.input_lines()
    wires = [l.split(',') for l in lines]
    print(solve(wires))


