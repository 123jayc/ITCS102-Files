for i in range(1, 10, 1):
    for x in range(10, i, -1):
        print('o', end='')
    for y in range(1, i + 1):
        print('i', end = '')
    print()
    