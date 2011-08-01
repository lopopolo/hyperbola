from django.template import Library

register = Library()

def sorted_dict_keys(dict):
    return sorted(self.d.keys())
register.filter('sorted_dict_keys', sorted_dict_keys)

def dict_get(dict, key):
    return dict[key]
register.filter('dict_get', dict_get)
