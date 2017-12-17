from django import template
from django.template.defaultfilters import stringfilter
from decimal import *


register = template.Library()


@register.filter(name='to_add')
def to_add(value, num):
    a = float(value)+float(num)
    return Decimal(a).quantize(Decimal('0.00'))