def pythagorean_checker(a, b, c):
    return c ** 2 == a ** 2 + b ** 2


def triangle_checker(a, b, c):
    sides = [a, b, c]
    s = sum(sides)
    for side in sides:
        if s - side < side:
            return False
    return True


if __name__ == '__main__':
    print(pythagorean_checker(3, 4, 5))
    print(pythagorean_checker(3, 8, 5))
    print(pythagorean_checker(5, 12, 13))

    print(triangle_checker(1, 1, 20))
    print(triangle_checker(3, 8, 5))
    print(triangle_checker(5, 12, 13))

