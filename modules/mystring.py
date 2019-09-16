import string


def scoring_calculation(word=''):
    """Calculate scoring index for word
    where is 'a' = 1, 'b' = 2 etc. """
    return sum(
        [string.ascii_lowercase.index(str(symbol)) + 1
         for symbol in word]
    )


def high(s=''):
    """Function returns high score word"""
    scores = {word: scoring_calculation(word) for word in s.split()}
    return sorted(scores.items(), key=lambda x: x[1], reverse=True)[0][0]


def first_non_repeating_latter(string):
    """Function returns the first character that is not repeated
    anywhere in the string."""
    for l in string:
        if string.lower().count(l.lower()) == 1:
            return l
    return ''
