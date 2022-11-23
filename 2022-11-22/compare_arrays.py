def comp(array1, array2):
    """Return boolean value of comparing arrays: True if elements in
    array2 are the elements in array1 squared, regardless of the order; 
    False otherwise, or if array1 or array2 is None.
    """
    if array1 and array2:
        return sorted([num * num for num in array1]) == sorted(array2)
    return array1 == array2 == []
