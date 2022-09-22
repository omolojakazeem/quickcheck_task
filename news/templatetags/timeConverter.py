from django import template
from datetime import datetime
register = template.Library()


@register.filter
def time_converter(unix_val):

    ts = int(unix_val)
    time = datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    return time
