def sum_pairs(ints, s):
    len_ints = indice = len(ints)
    pairs = []
    for i in range(len_ints):
        for j in range(i + 1, len_ints):
            if ints[i] + ints[j] == s and j <= indice:
                indice = j
                pairs.clear()
                pairs.append(ints[i])
                pairs.append(ints[j])

    if len(pairs):
        return pairs
