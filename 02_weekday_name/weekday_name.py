def weekday_name(day_of_week):
    """Return name of weekday.
    
        >>> weekday_name(1)
        'Sunday'
        
        >>> weekday_name(7)
        'Saturday'
        
    For days not between 1 and 7, return None
    
        >>> weekday_name(9)
        >>> weekday_name(0)
    """

    if day_of_week < 1 or day_of_week > 7:
        return None

    weekday_list = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

    for day in weekday_list:
        if weekday_list.index(day) == day_of_week-1:
            return day
    return None # Sanity check