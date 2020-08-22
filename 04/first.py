import aoc.input


def valid(password):
    last = -1
    seenDouble = False
    double = False
    doubleNum = -1
    for p in password:
        if int(p) < last:
            return False
        if int(p) == last:
            if int(p) == doubleNum:
                print("F")
                double = False
            else:
                if double:
                    seenDouble = True
                print("T")
                double = True
            doubleNum = int(p)
        last = int(p)
    return seenDouble or double


if __name__ == "__main__":
    min = 146810
    max = 612564

    vallid = 0
    for password in range(max - min):
        password += min
        password = str(password)
        if valid(password):
            vallid += 1
    print(vallid)



