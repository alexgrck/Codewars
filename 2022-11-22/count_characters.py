from collections import Counter

def count(string):
    """Return counted all the occuring characters in a string. Return {} if
    the string is empty.
    """
    return dict(Counter(string))