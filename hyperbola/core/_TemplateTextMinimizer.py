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

from __future__ import print_function

import re

from ._ManageMinimizers import get_minimizers

FLAGS = re.IGNORECASE + re.DOTALL

EXCLUDE = r'({#\s*NOMINIFY\s*#})(.*?)({#\s*ENDNOMINIFY\s*#})'
REMOVE = r'({%\s*COMMENT\s*%})(.*?)({%\s*ENDCOMMENT\s*%})'  # Tag Comments
REMOVE2 = r'({#[^\n\r]+#})'  # Other Comments
DVAR = r'({{[^\n\r]+}})'  # Django variable
DTAG = r'({%[^\n\r]+%})'  # Django tag
SCRIPT = r'(<SCRIPT\b[^>]*>)(.*?)(</SCRIPT>)'
STYLE = r'(<STYLE\b[^>]*>)(.*?)(</STYLE>)'

RE_EXCLUDE = re.compile(EXCLUDE, flags=FLAGS)
RE_REMOVE = re.compile(REMOVE, flags=FLAGS)
RE_REMOVE2 = re.compile(REMOVE2, flags=FLAGS)
RE_DVAR = re.compile(DVAR, flags=FLAGS)
RE_DTAG = re.compile(DTAG, flags=FLAGS)

# Will encasing the key in quotes. Will work well with javascript minifiers?
KEY = '_~%s~_'

HTMLMINIMIZERS = get_minimizers()


def minimize_template_text(text):
    """
    Take a Django template text and returns a minified version.

    Performance is not critical as this function should be run off-line
    to store minimized templates.

    Use the {# NOMINIFY #} {# ENDNOMINIFY #} comment tags to wrap code you do
    not want minified.  Suggested uses include wrapping pre, code, and textarea
    html tags as well as the example above.
    """
    # Create a list to hold special values temporarily removed
    # from the text.
    # format -> [(key, value), ...]
    word_list = []

    # Remove Excluded text
    excludes = RE_EXCLUDE.findall(text)

    # Strip out the {# NOMINIFY #} and {# ENDNOMINIFY #} tags
    excludes_find = [''.join(x) for x in excludes]
    excludes_replace = [x[1] for x in excludes]

    # replace excluded text with keys and populate word_list
    text = substitute_text(text, word_list, KEY, excludes_find, excludes_replace)

    # Remove any remaining template comments
    text = RE_REMOVE.sub('', text)
    text = RE_REMOVE2.sub('', text)

    # We want to "protect" Django Vars and Tags
    # then treat scripts and styles after "protecting" Django Vars and tags

    # Extract Django Variables
    dvars = RE_DVAR.findall(text)

    # replace Django Variables text with keys and populate word_list
    text = substitute_text(text, word_list, KEY, dvars)

    # Extract django tags
    dtags = RE_DTAG.findall(text)

    # replace Django Tags text with keys and populate word_list
    text = substitute_text(text, word_list, KEY, dtags)

    # Run HTML Minimizers
    def run_html_minimizer(minimizers, content):
        """Go loop for running HTML minimizers."""
        if not minimizers:
            return content
        minimizers = list(minimizers)
        to_run = minimizers.pop(0)
        return run_html_minimizer(minimizers, to_run(content))

    text = run_html_minimizer(HTMLMINIMIZERS, text)

    # put values back into text
    text = revert_text_keys(text, word_list)

    return text.strip()


def revert_text_keys(text, word_list):
    """
    Revert the text keys.

    We may have to do this multiple times as some keys may be embeded in
    other word_list entries.
    """
    if not text or not word_list:
        return text

    # If we loop through the word_list 10 times without
    #   consuming it completely, then something's probably wrong.

    max_iterations = len(word_list) * 10

    for _iteration in range(max_iterations):

        # When the wordlist empties, break the for loop
        if not word_list:
            break

        # Take the first entry off the list
        key, value = word_list.pop(0)

        if key in text:
            # Replace the key with the value
            text = text.replace(key, value)
        else:
            # Put the entry back at the end of the list
            word_list.append((key, value))
    else:
        # We looped through too many time and
        # never consumed the whole word_list
        raise Exception('Minimizer failed to find all embeded variables.\n'
                        '%s\n%s' % (word_list, text))

    return text


def substitute_text(text, word_list, key_template,
                    find_list, substitute_list=None):
    """
    Substitute the first occurence of each entry in find_list with a key.

    Store the key and value in the substitute_list in the word_list.  If no
    substitute_list is provided, use the value in the find list.
    """
    if not substitute_list:
        substitute_list = find_list

    values_list = zip(find_list, substitute_list)

    for find, substitute in values_list:
        key = key_template % len(word_list)
        text = text.replace(find, key, 1)
        word_list.append((key, substitute))

    return text
