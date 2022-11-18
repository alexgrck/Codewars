import re

def to_camel_case(text: str):
    """Return converted dash/underscore delimited words into camel casing.
    The first word within the output is capitalized only if the original word 
    is capitalized. The next words are always capitalized.
    """
    splitted = re.split(r"[-_]", text)
    return splitted[0] + ''.join([word.capitalize() for word in splitted[1:]])

