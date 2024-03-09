import logging
import operator
from django import template
from django.db.models import Model
from django.core.cache import cache
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe

_logger = logging.getLogger(__name__)
register = template.Library()


@register.simple_tag(name='combine_templates')
def combine_templates(template_name, request=None):
    html = cache.get(template_name, '')
    if html:
        return mark_safe(html)
    for app in settings.INSTALLED_APPS:
        try:
            html += render_to_string(
                f'{app.split(".")[-1]}/{template_name}', request=request
            )
        except template.TemplateDoesNotExist:
            continue
    cache.set(template_name, html, 60 * 15)
    return mark_safe(html)


@register.filter(name='get_attr')
def get_attr_from_string(param: object, value: str):
    try:
        attr = operator.attrgetter(value)(param)
    except AttributeError:
        _logger.exception(f'Object {param} has no attribute {value}')
        return ''
    if attr is None:
        return None
    if callable(attr):
        return mark_safe(attr())
    else:
        return mark_safe(attr)


@register.filter(name='related_obj_url')
def related_obj_url(param: object, value: str):
    attr = getattr(param, value, False)
    if attr:
        return attr.get_absolute_url()
    return '#'


@register.filter(name='message_class')
def message_class(param):
    if param.level == 25:
        return 'is-success'
    if param.level == 30:
        return 'is-warning'
    if param.level == 40:
        return 'is-danger'
