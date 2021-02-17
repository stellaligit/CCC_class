for i in range(5):
    field = [*input()]
    print(*field, sep='')
    b = []
    for x, y in enumerate(field):
        if y == '.':
            continue
        else:
            b.append([int(y), x])

    for j in range(4):
        # for i in b:
        #     i[1] += i[0]
        b = list(map(lambda(i: i[1] += i[0]), b))

        n = len(field)
        field = ['.'] * n
        for i in b:
            if i[1] >= n:
                continue
            elif field[i[1]] != '.':
                field[i[1]] += i[0]
            else:
                field[i[1]] = i[0]

        print(*field, sep='')
