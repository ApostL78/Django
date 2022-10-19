from django import template

from body.models import Categories, Task
from django.db.models import *

register = template.Library()


@register.simple_tag
def get_categories():
    return Categories.objects.all()


@register.simple_tag
def get_tasks():
    return Task.objects.all()


@register.inclusion_tag('body/category.html')
def show_categories():
    # categories = Categories.objects.all()
    categories = Categories.objects.annotate(cnt=Count('task')).filter(cnt__gt=0)
    return {
        'categories': categories,
    }
