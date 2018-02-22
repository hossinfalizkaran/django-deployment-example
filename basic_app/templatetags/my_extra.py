from django import template

register = template.Library()


def ct(value,arg):
    """""
    this cuts out
    """""
    return value.replace(arg,'')
register.filter('ct',ct)
