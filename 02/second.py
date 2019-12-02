import aoc.input


def run(cells, noun, verb):
    pointer = 0
    cells[1] = noun
    cells[2] = verb

    while True:
        op = cells[pointer]

        if op == 99:
            break
        elif op == 1:
            cells[cells[pointer+3]] = cells[cells[pointer+1]]+cells[cells[pointer+2]]
        elif op == 2:
            cells[cells[pointer+3]] = cells[cells[pointer+1]]*cells[cells[pointer+2]]
        else:
            print("Unknown code", op)
            return None

        pointer += 4

    return cells[0]


if __name__ == "__main__":
    cells = [int(a) for a in aoc.input.input_lines()]

    for noun in range(100):
        for verb in range(100):
            res = run(cells[:], noun, verb)
            print(res - 19690720)
            if res == 19690720:
                print("Found it!")
                print(noun)
                print(verb)
                exit(0)


