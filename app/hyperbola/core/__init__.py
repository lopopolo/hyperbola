from django.utils.deconstruct import deconstructible

__all__ = ("hash_with_extension", "make_escape_function", "MakeUploadTo", "views")


def make_escape_function(autoescape=True):
    """
    Create an escape function based on the desired autoescape behavior.

    Args:
        autoescape (bool): Whether or not this template tag should escape text
    """
    from django.utils.html import conditional_escape
    if autoescape:
        return conditional_escape
    else:
        return lambda x: x


def hash_with_extension(generator):
    """
    A namer for a imagekit.spec.ImageSpec that names files {prefix}/hash.extension.

    A namer that, given the following source file name::

        photos/thumbnails/bulldog.jpg

    will generate a name like this::

        /path/to/generated/images/5ff3233527c5ac3e4b596343b440ff67.jpg

    where "/path/to/generated/images/" is the value specified by the
    ``IMAGEKIT_CACHEFILE_DIR`` setting.

    Args:
        generator (imagekit.specs.ImageSpec): generator spec for the requested image.
    """
    import os

    from django.conf import settings
    from imagekit.utils import suggest_extension

    source_filename = getattr(generator.source, 'name', None)
    ext = suggest_extension(source_filename or '', generator.format).lower()
    return os.path.normpath(os.path.join(settings.IMAGEKIT_CACHEFILE_DIR,
                                         '%s%s' % (generator.get_hash(), ext)))


@deconstructible
class MakeUploadTo(object):
    """Make a Django FileField upload_to callable that names files with a uuid."""

    def __init__(self, prefix):
        self.prefix = prefix

    def __call__(self, instance, filename):
        import os
        import uuid

        del instance

        _, extension = os.path.splitext(filename)
        mangled_name = "{}{}".format(uuid.uuid4().hex, extension)
        return os.path.join(self.prefix, mangled_name)
