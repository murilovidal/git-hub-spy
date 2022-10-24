from datetime import datetime
from django import template

register = template.Library()

@register.filter(name='convert_str_date')
def convert_str_date(value):
    return str(datetime.strptime(value, '%Y-%m-%dT%H:%M:%SZ').strftime("%Y/%m/%d - %H:%M:%S"))