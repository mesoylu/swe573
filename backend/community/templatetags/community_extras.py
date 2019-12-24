from django import template

register = template.Library()


@register.filter(name='get_url')
def get_url(value, arg):
    splitted = value.split(arg)
    return splitted[-1]