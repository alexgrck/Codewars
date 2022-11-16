def disemvowel(string_: str):
    """Return string value without vowels (except letter "y" - according to
    challenge description)."""
    return ''.join([l for l in string_ if l not in "aeiouAEIOU"])