def unpack(res):
    def foo(st, startPoint):
        return [st[i] for i in range(startPoint, len(st), 2)]
    letters = foo(res, 0)
    numbers = foo(res, 1)
    return ''.join(l * int(n) for l, n in zip(letters, numbers))

if __name__ == '__main__':
    print(unpack("a3v3f1d1f2"))
    print(unpack("a1v1t1v3f2"))
