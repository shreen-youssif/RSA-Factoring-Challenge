#!/usr/bin/python3
import sys


def factorize(num):
    for i in range(2, num):
        if num % i == 0:
            return i, num // i
    return None

def main(file_path):
    with open(file_path, 'r') as file:
        numbers = file.read().splitlines()

    for num in numbers:
        num = int(num)
        factors = factorize(num)
        print(f"{num}={factors[0]}*{factors[1]}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)

    file_path = sys.argv[1]
    main(file_path)

