def alarm(a, b, c):
    d = False
    if (b - a) > 100 or (c - b) > 200:
        d = not d
    return d


if __name__ == '__main__':
    a = 300
    b = 400
    c = 60
    e = alarm(a, b, c)
    print(e)
