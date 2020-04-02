def sorted_and_multiplied(l, m=1):
    return [i * m for i in sorted(l, reverse=True)]


if __name__ == '__main__':
    print(sorted_and_multiplied([14, 57, 93, 1], 8))
    print(sorted_and_multiplied([8, 23, 4, 11], 2))
    print(sorted_and_multiplied([33, 45, 7, 101]))
