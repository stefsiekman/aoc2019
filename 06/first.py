import aoc.input
from queue import Queue


class Planet:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children = []


def create_planet(planets, name):
    if name in planets:
        return planets[name]
    else:
        p = Planet(name)
        planets[name] = p
        return p


if __name__ == "__main__":
    lines = aoc.input.input_lines()
    planets = dict()
    for line in lines:
        line_planets = line.split(')')

        p1 = create_planet(planets, line_planets[0])
        p2 = create_planet(planets, line_planets[1])

        p2.parent = p1
        p1.children.append(p2)

    queue = Queue()
    queue.put((0, planets["COM"]))

    total = 0

    while not queue.empty():
        depth, planet = queue.get()
        total += depth

        for c in planet.children:
            queue.put((depth + 1, c))

    print(total)

    queue = Queue()
    queue.put((0, planets["YOU"].parent))

    visited = set()

    while not queue.empty():
        distance, planet = queue.get()
        visited.add(planet)
        found = any(c.name == "SAN" for c in planet.children)
        if found:
            print(distance)

        if planet.parent is not None and planet.parent not in visited:
            queue.put((distance + 1, planet.parent))

        for c in planet.children:
            if c not in visited:
                queue.put((distance + 1, c))




