def number_operations(a):
    l = [i for i in a if i in range(10, 100)]
    return [sum(l) / len(l), min(l), max(l), sum(l)]


def list_operations(l):
    return [number_operations(i) for i in l]


if __name__ == '__main__':
    data = [
        [1, 10, 34, 110, 400, 30, 20],
        [-5, -10, 55, 120, 30],
        [2, 67, 23, 78, 200],
    ]
    print(*list_operations(data), sep="\n")
    print('\n')
    data = [
        [-1, 45, 23, 32, 999],
        [67, 99, 23],
        [23],
    ]
    print(*list_operations(data), sep="\n")
