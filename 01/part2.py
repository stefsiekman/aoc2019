import aoc.input


def fuel_rec(weight):
    total = weight
    last = weight

    while last // 3 - 2 > 0:
        last = last // 3 - 2
        total += last

    return total


if __name__ == "__main__":
    print(sum(fuel_rec(int(line.strip()) // 3 - 2)
              for line in aoc.input.input_lines()))

