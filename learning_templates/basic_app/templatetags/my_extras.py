from django import template

register = template.Library()

@register.filter(name='cut_two')
def cut_two(value,arg):
    """
    Cuts off all args from value string.
    """
    return value.replace(arg,'')

# register.filter('cut_two',cut_two)
