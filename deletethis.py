with open("input.txt") as file:
    print(tuple(line.rstrip() for line in file))