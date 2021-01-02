from datetime import datetime
from django import template
from django.conf import settings


register = template.Library()


@register.filter
def format_date(value):
    return datetime.utcfromtimestamp(int(value))  # .strftime(settings.DAY_FORMAT)
