def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    return ''.join([swapCase(char) if char.lower() == to_swap.lower() else char for char in phrase])

def swapCase(char):
   """Swaps the case of individual character [char] in string."""
   return char.lower() if char.isupper() else char.upper()