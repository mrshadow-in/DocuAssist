# Create a Python file named custom_filters.py in your app's templatetags directory.
# Inside custom_filters.py, define your custom filter.

from django import template

register = template.Library()


@register.filter
def split_message(value):
    # Split the value by ': ' and return the second part
    return value.split(': ')[1]
