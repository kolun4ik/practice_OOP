from collections import Counter


def sum_pairs(ints, s):
    pairs = []
    out = None

    # 1. отсортировать список
    # 2. Обрезать список до позиции, в котрой искомая сумма будет превышена
    # 3. вычленить пары, дающие в сумме заданное число
    # 3. Взять пару, у которой второй индекс в  массиве ints минимальный.
    # 4. Если в паре одинаковые значения, то взять индекс второго значенмя
    # (ints.index(n, )
    sort = sorted(ints)

    for i in range(1, len(sort)):
        if sort[0] + sort[i] > s:
            break

    reduce = sort[:i + 1]
    for j in range(len(reduce)):
        for k in range(j + 1, len(reduce)):
            if reduce[j] + reduce[k] == s:
                if ints.index(reduce[j]) < ints.index(reduce[k]):
                    pairs.append([reduce[j], reduce[k]])
                else:
                    pairs.append([reduce[k], reduce[j]])

    if len(pairs):
        indice = len(ints)
        print(pairs)
        for pair in pairs:
            if pair[0] == pair[1]:
                i = ints.index(pair[1], ints.index(pair[1]) + 1)
            else:
                i = ints.index(pair[1])

            if i <= indice:
                out = list(pair)
                indice = i
        # print('Out:', out)
    return out
