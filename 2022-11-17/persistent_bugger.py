def persistence(num: int):
    """Return multiplicative persistence (which is the number of times you 
    must multiply the digits in num until you reach a single digit) of 
    a positive integer.
    """
    if num < 10:
        return 0
    multiplied_num = 1
    for i in str(num):
        multiplied_num *= int(i)
    return 1 + persistence(multiplied_num)