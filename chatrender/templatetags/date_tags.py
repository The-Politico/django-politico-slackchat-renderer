from django import template
from django.utils.dateparse import parse_datetime

register = template.Library()


@register.filter(name="timestamp")
def timestamp_filter(value):
    return parse_datetime(value)
