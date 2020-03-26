def pythagorean_checker(a, b, c):
    return c ** 2 == a ** 2 + b ** 2


if __name__ == '__main__':
    print(pythagorean_checker(3, 4, 5))
    print(pythagorean_checker(3, 8, 5))
    print(pythagorean_checker(5, 12, 13))
