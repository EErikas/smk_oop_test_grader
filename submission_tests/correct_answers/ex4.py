def pack(string):
    res = ""
    count = 1
    res += string[0]
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            count += 1
        else:
            res += str(count)
            res += string[i + 1]
            count = 1
    res += str(count)
    return res


if __name__ == '__main__':
    print(pack("aaavvvfdff"))
    print(pack("avtvvvff"))
