def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    return {ltr: phrase.lower().count(ltr) for ltr in phrase.lower() if ltr == 'a' or ltr == 'e' or ltr == 'i' or ltr == 'o' or ltr == 'u'}