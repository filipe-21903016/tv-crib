from django import template
import hashlib

register = template.Library()


@register.filter(name='split')
def split(str):
    return str.split('\\')


@register.filter(name='hash')
def hash(str):
    return hashlib.sha224(bytes(str, 'utf-8')).hexdigest()