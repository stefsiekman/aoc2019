import requests
import os.path
import datetime
import aoc.tokens


def input_url(day):
    return f"https://adventofcode.com/2019/day/{day}/input"


def download(day):
    res = requests.get(input_url(day), cookies=aoc.tokens.tokens)

    return res.status_code, res.text


def cached(day):
    text = None

    if os.path.exists("input.txt"):
        print("Using cached input...")
        with open("input.txt", "r") as file:
            text = file.read()
    else:
        print("Downloading input...")
        code, text = download(day)
        if code == 200:
            with open("input.txt", "w") as file:
                file.write(text)
        else:
            print("WARNING: Non 200 code")

    print(f"Read input of {len(text) / 1000} kB")
    print(f"... with {len(text.split())} lines")
    print()

    return text


def input_text(day=datetime.datetime.today().day):
    return cached(day)


def input_lines():
    return input_text().split(',')


if __name__ == "__main__":
    print(input_lines())
