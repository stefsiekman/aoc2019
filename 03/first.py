import aoc.input


dirs = {
    "D": (0, -1),
    "U": (0, 1),
    "R": (1, 0),
    "L": (-1, 0)
}


def nodes(wire):
    visited = set()
    position = (0, 0)

    for movement in wire:
        delta = dirs[movement[0]]
        amount = int(movement[1:])
        for _ in range(amount):
            new_position = (position[0] + delta[0], position[1] + delta[1])
            visited.add(new_position)
            position = new_position

    return visited


def distance(p):
    return abs(p[0]) + abs(p[1])


def closest_crossing(visited):
    closest_distance = None
    closest_position = None
    for pos in visited[0]:
        if pos in visited[1]:
            dist = distance(pos)
            if closest_distance is None or closest_distance > dist:
                closest_distance = dist
                closest_position = pos

    return closest_position


if __name__ == "__main__":
    lines = aoc.input.input_lines()
    wires = [l.split(',') for l in lines]
    wire_nodes = [nodes(w) for w in wires]
    print(distance(closest_crossing(wire_nodes)))

