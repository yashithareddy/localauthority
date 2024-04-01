import json
from django import template

register = template.Library()

@register.filter
def json_encode(obj):
    return json.dumps(obj)
