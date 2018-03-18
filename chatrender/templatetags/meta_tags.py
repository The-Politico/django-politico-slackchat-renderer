import re
from urllib.parse import urljoin

from django import template

register = template.Library()


@register.filter(name="url_join")
def url_join_filter(base, path):
    return urljoin(base, re.sub(r'^/', '', path))
