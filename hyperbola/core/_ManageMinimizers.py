"""
Copyright (c) 2012 Charles Kaminski (CharlesKaminski@gmail.com).

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.
"""

import re

from django.conf import settings

FLAGS = re.IGNORECASE + re.DOTALL

SPACE = r'(\s+)'
TAGS = r'(>\s+<)'

RE_SPACE = re.compile(SPACE, flags=FLAGS)
RE_TAGS = re.compile(TAGS, flags=FLAGS)


def collapse_spaces(text):
    return RE_SPACE.sub(' ', text)


def collapse_end_start_tag(text):
    return RE_TAGS.sub('><', text)


def get_minimizers():
    """Return a list of htmlminimizers."""
    # Initialize
    htmlminimizers = [collapse_spaces, collapse_end_start_tag]

    if hasattr(settings, 'AGGRESSIVE_HTML_MINIMIZER'):
        aggressive = settings.AGGRESSIVE_HTML_MINIMIZER
        if not aggressive:
            htmlminimizers.pop()

    # Get any override settings
    if hasattr(settings, 'HTML_MINIMIZERS'):
        htmlminimizers = settings.HTML_MINIMIZERS

    # Check that they are lists or tuples
    if not isinstance(htmlminimizers, (list, tuple)):
        raise Exception('Minimizers must be enclosed in a list or tuple.\n'
                        'Check your django settings file')
    for minimizer in htmlminimizers:
        if not callable(minimizer):
            raise Exception('Minimizers must be callable functions.\n'
                            'Check your django settings file')

    # Convert any tuples into lists
    return list(htmlminimizers)