from django import template


register = template.Library()

@register.filter
def cut_description(value, arg):
    arg = int(arg)
    if len(value) > arg:
        while value[arg] != ' ' and arg > 0:
            arg -= 1
        if arg <= 0:
          return value
        return value[:arg] + ' ...'