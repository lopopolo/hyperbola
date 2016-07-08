from django.utils.html import conditional_escape


def make_escape_function(autoescape=True):
    """
    Create an escape function based on the desired autoescape behavior

    Args:
        autoescape: Whether or not this template tag should escape text
    """
    if autoescape:
        return conditional_escape
    else:
        return lambda x: x
