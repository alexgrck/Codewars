# Write simple .camelCase function for strings. All words must have their first 
# letter capitalized without spaces.

# A word from me: according to description, function is expected to return
# PascalCased string, and as such the function is tested at Codewars testing
# interface. I decided to comment this function and create new one, returning
# correct camelCased string.

# def camel_case(string: str):
#     """Return CamelCased string from given string value."""
#     return ''.join([word.capitalize() for word in string.split()])

def camel_case(string: str):
    """Return camelCased string from given string value."""
    return string.lower().split()[0] + ''.join([word.capitalize() for word in string.lower().split()[1:]])