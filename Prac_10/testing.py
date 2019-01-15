import doctest

from Prac_10.car import Car

def repeat_string(s, n):
    return " ".join([s] * n)
def is_long_word(word, length=5):
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length
