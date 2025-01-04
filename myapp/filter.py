def format_datetime(value, fmt='%Y-%m-%d %p %I:%M'):
    """
    A custom template filter to format datetime objects in Jinja templates.
    
    Args:
        value (datetime): The datetime object to format.
        fmt (str): The formatting string. Default is '%Y-%m-%d %p %I:%M'.
    
    Returns:
        str: The formatted datetime string.
    """
    return value.strftime(fmt)