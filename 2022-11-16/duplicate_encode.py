def duplicate_encode(word: str):
    """Return a new string from given string modified in the following manner:
    each character in the new string is "(" if that character appears only once 
    in the original string, or ")" if that character appears more than once in 
    the original string (ignore capitalization when determining if a character 
    is a duplicate."""
    return ''.join(["(" if word.lower().count(char) == 1 else ")" for char in word])

    # BEFORE REFACTORING
    # lowercased = word.lower()
    # for letter in lowercased:
    #     how_many_times = lowercased.count(letter)
    #     if how_many_times == 1:
    #         result += "("
    #     elif how_many_times > 1:
    #         result += ")"
    # return result





