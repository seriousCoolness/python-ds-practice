def includes(collection, sought, start=None):
    """Is sought in collection, starting at index start?

    Return True/False if sought is in the given collection:
    - lists/strings/sets/tuples: returns True/False if sought present
    - dictionaries: return True/False if *value* of sought in dictionary

    If string/list/tuple and `start` is provided, starts searching only at that
    index. This `start` is ignored for sets/dictionaries, since they aren't
    ordered.

        >>> includes([1, 2, 3], 1)
        True

        >>> includes([1, 2, 3], 1, 2)
        False

        >>> includes("hello", "o")
        True

        >>> includes(('Elmo', 5, 'red'), 'red', 1)
        True

        >>> includes({1, 2, 3}, 1)
        True

        >>> includes({1, 2, 3}, 1, 3)  # "start" ignored for sets!
        True

        >>> includes({"apple": "red", "berry": "blue"}, "blue")
        True
    """
    if type(collection) == dict:
        for (k, v) in collection.items():
            if v == sought:
                return True
        return False
    elif type(collection) == set:
        return sought in collection
    elif type(collection) == str:
        return True if collection.find(sought, start if start != None else 0, len(collection)) != -1 else False
    elif type(collection) == list:
        for i in range(start if start != None else 0, len(collection)):
            if collection[i] == sought:
                return True
        return False
    elif type(collection) == tuple:
        for i in range(start if start != None else 0, len(collection)):
            if collection[i] == sought:
                return True
        return False
    

