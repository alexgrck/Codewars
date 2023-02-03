def spin_words(expression: str):
    """Return a string where words with five or more letters are reversed."""
    return " ".join(
        [word[::-1] if len(word) >= 5 else word for word in expression.split()]
    )
