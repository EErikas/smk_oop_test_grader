def is_int(s, base=10):
    try:
        int(s, base)
        return True
    except ValueError:
        return False


def calculate(b, d, o):
    s = 0
    if is_int(b, 2):
        s += int(b, 2)
        if is_int(d):
            s += int(d)
            if is_int(o, 8):
                s += int(o, 8)
                return 'The result is {} in hex or {} in dec'.format(hex(s), s)
            return '{} is not a valid octal integer'.format(o)
        return '{} is not a valid decimal integer'.format(d)
    return '{} is not a valid binary integer'.format(b)


if __name__ == '__main__':
    print(calculate('10', '10', '10'))
    print(calculate('12', '43', '2'))
    print(calculate('101', 'a', '11'))
    print(calculate('1', '20', 'z'))
    print(calculate('10', '85', '11'))
