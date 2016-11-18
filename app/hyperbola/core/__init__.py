from django.utils.deconstruct import deconstructible
from imagekit.registry import register
from imagekit.specs import ImageSpec

__all__ = ("hash_with_extension", "make_escape_function", "MakeUploadTo", "RetinaThumbnail", "views")


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
                                         '{}{}'.format(generator.get_hash(), ext)))


class RetinaThumbnail(ImageSpec):
    """
    A retina-scaled generating thumbnail class.

    Accepts an additional keyword argument over the default imagekit
    thumbnail, retina_scale. All values of retina_scale map to the same
    basename with an e.g. @2x specifier.

    Also sets saner defaults for crop (0) and upscale (False).
    """

    def __init__(self, width=None, height=None, anchor=None, crop=0, upscale=False, retina_scale=1, **kwargs):
        from imagekit.processors import Thumbnail as ThumbnailProcessor
        self.multiplier = retina_scale
        self.processors = [ThumbnailProcessor(width * self.multiplier, height * self.multiplier, anchor=anchor,
                                              crop=crop, upscale=upscale)]
        super(RetinaThumbnail, self).__init__(**kwargs)

    @property
    def cachefile_name(self):
        import os

        source_filename = super(RetinaThumbnail, self).cachefile_name
        name, extension = os.path.splitext(source_filename)
        if self.multiplier == 1:
            return "{}{}".format(name, extension)
        return "{}@{}x{}".format(name, self.multiplier, extension)

    def get_hash(self):
        from imagekit import hashers

        return hashers.pickle([
            self.source.name,
            self.format,
            self.options,
            self.autoconvert,
        ])


register.generator('hyperbola:thumbnail', RetinaThumbnail)


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
