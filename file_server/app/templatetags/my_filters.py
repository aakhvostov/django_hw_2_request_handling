from datetime import datetime
from django import template


register = template.Library()


@register.filter
def format_date(value):
    return datetime.utcfromtimestamp(int(value))
