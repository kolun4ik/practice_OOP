from itertools import permutations as pm


def permutations(string):
    return [''.join(item) for item in set(pm(string, len(string)))]
