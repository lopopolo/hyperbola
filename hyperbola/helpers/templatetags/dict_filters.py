from django.template import Library, Node
import re

register = Library()

def sorted_dict_keys(parser, token):
  # This version uses a regular expression to parse tag contents.
  try:
    # Splitting by None == splitting by spaces.
    tag_name, arg = token.contents.split(None, 1)
  except ValueError:
    raise template.TemplateSyntaxError("%r tag requires arguments" % token.contents.split()[0])
  m = re.search(r'(.*?) as (\w+)', arg)
  if not m:
    raise template.TemplateSyntaxError("%r tag had invalid arguments" % tag_name)
  d, var_name = m.groups()
  return FilterNode(sorted(d.keys()), name)
register.tag('sorted_dict_keys', sorted_dict_keys)

def dict_get(parser, token):
  # This version uses a regular expression to parse tag contents.
  try:
    # Splitting by None == splitting by spaces.
    tag_name, arg = token.contents.split(None, 1)
  except ValueError:
    raise template.TemplateSyntaxError("%r tag requires arguments" % token.contents.split()[0])
  m = re.search(r'(.*?) (.*?) as (\w+)', arg)
  if not m:
    raise template.TemplateSyntaxError("%r tag had invalid arguments" % tag_name)
  d, key, var_name = m.groups()
  return FilterNode(d[key], name)
register.tag('dict_get', dict_get)

class FilterNode(Node):
  def __init__(self, val, name):
    self.val = val
    self.name = name
  def render(self, context):
    context[self.name] = self.val
    return ''

