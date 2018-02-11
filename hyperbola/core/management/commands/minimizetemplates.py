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

from optparse import make_option
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand
from django.template.loaders.app_directories import get_app_template_dirs

from ..._TemplateTextMinimizer import minimize_template_text

ARCHIVE = '_minimizer_archive'


class Command(BaseCommand):
    help = '''Use this tool to minimize Django templates after
development.  This way, your templates are small when they are
evaluated and the HTML served is already minimized; eliminiating
any post-processing minimization step.

Use the comment tags {# NOMINIFY #} {# ENDNOMINIFY #} to wrap
content you do not want minified.

Uses the setting TEMPLATES in your Django settings file and
    `get_app_template_dirs` to tell the command where to find
    templates to minimize.

Customization:
The minimizer command uses its own minimizers for html, style tag embeded
    css, and script tag embeded javascript. You can override these and chain
    any number of your own minimizers using settings below.  These
    settings go in the Django settings file. Custom minimizers must
    be functions that accept text as a string parameter and return
    text as a string.
    JAVASCRIPT_MINIMIZERS = [custom_function1, custom_function2,]
    CSS_MINIMIZERS        = [custom_function3, custom_function4,]
    HTML_MINIMIZERS       = [custom_function5, custom_function6,]

    To turn off a minimizer, use the following pattern:
    f = lambda x: x
    JAVASCRIPT_MINIMIZER = [f,]

You can tell the minimizer command to disable an aggressive minimizer
    in the default HTML minimizer chain.  This minimizer normally removes
    (instead of just collapsing) the remaining space between '>' & '<'
    character.  Set the following setting to False in your Django
    settings file to disable this final step:
    AGGRESSIVE_HTML_MINIMIZER = False

Method - For each template, the minimizer command:
1. Replaces any {# NOMINIFY #} {# ENDNOMINIFY #} content with
    a unique identifier and saves the content in memory so that
    it is excluded from the rest of the process.
2. Remaining Django comments are removed.
3. Django tags and django variables are replaced with with unique
    identifiers.  The tags and variables are saved in memory.
    This approach "protects" the tags and variables from the
    minimizers.  It also allows you to use Django tags and variables
    inside your javascript and CSS without ill effect by the
    CSS or javascript minimizer.
4. HTML script tags and content are replaced with unique
    identifiers. The tags and content are saved in memory for
    additional processing.  The type attribute for the script tag
    is checked to see if the script content is javascript.  If no
    type is provided, then javascript is assumed.  Any javascript
    is then run through the javascript minimizers.
5. An almost identical process to step 4 is implemented on the HTML
    style tags for css.
6. The remaining text (with the identifiers) is run through the
    html minimizers.
7. All of the content saved in memory and associated with unique
    identifiers are put back.
8. The original template is moved to an archive folder and replaced
    with the minimized template.

Limitations:
The minimizer does not handle script tags inside script tags or
    style tags inside style tags; an unusual occurance.
    eg: <script>bla bla <script> bla</script></script>
The minimizer collapses all white space not in a django tag,
    django variable, javascript, or inline css.  This includes
    whitespace inside <pre>, <textarea>, & similar tags, and
    whitespace inside html attributes.
Use the {# NOMINIFY #} {# ENDNOMINIFY #} comment tags to overcome
    these limiations.

'''
    _option_list = (
        make_option('-m', '--minimize',
                    action='store_true', dest='minimize', default=False,
                    help='Minimize templates.'),)

    def add_arguments(self, parser):
        option_typemap = {
            'string': str,
            'int': int,
            'float': float
        }
        for opt in self._option_list:
            option = {k: v
                      for k, v in opt.__dict__.items()
                      if v is not None}
            flags = (option.get('_long_opts', []) +
                     option.get('_short_opts', []))
            del option['_long_opts']
            del option['_short_opts']
            if 'type' in option:
                opttype = option['type']
                option['type'] = option_typemap.get(opttype, opttype)
            parser.add_argument(*flags, **option)

    def handle(self, *args, **options):
        # Reading template location from settings
        dirs = list(settings.TEMPLATES[0]['DIRS']) + \
            list(get_app_template_dirs('templates'))

        if options['minimize']:
            self.minimize_templates(dirs)
            self.stdout.write(self.style.SUCCESS('Successfully minimized '
                                                 'Templates:\n'))
            for template_dir in dirs:
                self.stdout.write('%s\n' % template_dir)
            return 0
        else:
            command_name = Path(__file__).name.rstrip('.py')
            self.print_help(command_name, '')

    def minimize_templates(self, dirs):
        template_dir_paths = [Path(d) for d in dirs]

        paths = []
        # Walk the directories to build a list of files to minimize
        # Currently not following symbolic links
        for template_dir in template_dir_paths:
            archive_dir = template_dir / ARCHIVE
            if archive_dir.exists():
                continue
            for template in template_dir.rglob('*.html'):
                paths.append((template_dir, template))

        # Minimize the files
        num_files, before, after = 0, 0, 0
        for template_root, template_path in paths:
            original = template_path.read_text()
            minimized = minimize_template_text(original)

            num_files = num_files + 1
            before = before + len(original)
            after = after + len(minimized)

            archive_path = template_root / ARCHIVE
            try:
                archive_path.mkdir()
            except FileExistsError:
                pass
            template_path.rename(archive_path / template_path.name)
            template_path.write_text(minimized)

        self.stdout.write('Files:    %s' % num_files)
        self.stdout.write('Before:   %s' % before)
        self.stdout.write('After:    %s' % after)
        self.stdout.write(
            'Decrease: {:.0%}'.format((before - after) / float(before)))
