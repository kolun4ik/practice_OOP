import string
from collections import defaultdict, Counter

def high(s=''):
    """Function returns high score word:
     if 'a'= 1', 'b' = 2 -> return 'b' """
    high_score = {}
    str_to_list = s.split()
    for word in str_to_list:
        score = 0
        for symbol in word:
            score += string.ascii_lowercase.index(str(symbol)) + 1
        high_score[word] = score
        high_score_word = sorted(high_score.items(), key=lambda x: x[1], reverse=True)
    return high_score_word[0][0]