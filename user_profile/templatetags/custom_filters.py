from base64 import b64encode
from django import template
register = template.Library()


@register.filter
def bin_2_img(_bin):
    if isinstance(_bin, bytes):
        return b64encode(_bin).decode('utf-8')
