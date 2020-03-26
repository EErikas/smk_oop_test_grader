def split_values(x, y):
    if isinstance(y, int) and y > 0 and len(x) % y == 0:
        return [''.join(sorted(set(x[i:i + y]))) for i in range(0, len(x), y)]
    return 'Error'


if __name__ == '__main__':
    x = "HABCDEFG"
    y = 2
    print(split_values(x, y))

    x = "AABCADAA"
    y = 4
    print(split_values(x, y))

    x = "AABCAAADA"
    y = "trys"
    print(split_values(x, y))

    x = "AABCAAADA"
    y = 5
    print(split_values(x, y))
