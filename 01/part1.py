import aoc.input


if __name__ == "__main__":
    print(sum(int(line.strip()) // 3 - 2
              for line in aoc.input.input_lines()))

