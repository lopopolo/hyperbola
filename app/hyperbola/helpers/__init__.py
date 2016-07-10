__all__ = ["hash_with_extension", "make_escape_function", "views"]


def make_escape_function(autoescape=True):
    """
    Create an escape function based on the desired autoescape behavior

    Args:
        autoescape: Whether or not this template tag should escape text
    """
    from django.utils.html import conditional_escape
    if autoescape:
        return conditional_escape
    else:
        return lambda x: x


def hash_with_extension(generator):
    """
    A namer that, given the following source file name::

        photos/thumbnails/bulldog.jpg

    will generate a name like this::

        /path/to/generated/images/5ff3233527c5ac3e4b596343b440ff67.jpg

    where "/path/to/generated/images/" is the value specified by the
    ``IMAGEKIT_CACHEFILE_DIR`` setting.

    """
    import os

    from django.conf import settings
    from imagekit.utils import suggest_extension

    source_filename = getattr(generator.source, 'name', None)
    ext = suggest_extension(source_filename or '', generator.format).lower()
    return os.path.normpath(os.path.join(settings.IMAGEKIT_CACHEFILE_DIR,
                                         '%s%s' % (generator.get_hash(), ext)))
