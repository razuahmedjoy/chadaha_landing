from django import template
register = template.Library()

@register.filter
def humanize_number(value):
    if value > 1000000000:
        return str(round(value/1000000000, 1)) + 'B'
    elif value > 1000000:
        return str(round(value/1000000, 1)) + 'M'
    elif value > 1000:
        return str(round(value/1000, 1)) + 'K'
    else:
        return value