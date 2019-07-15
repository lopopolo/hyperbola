from django.utils.deconstruct import deconstructible

__all__ = ("make_escape_function", "MakeUploadTo")


def make_escape_function(autoescape=True):
    """
    Create an escape function based on the desired autoescape behavior.

    Args:
        autoescape (bool): Whether or not this template tag should escape text

    """
    from django.utils.html import conditional_escape

    if autoescape:
        return conditional_escape
    return lambda x: x


@deconstructible
class MakeUploadTo:
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
