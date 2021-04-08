from django import template
from django.conf import settings

register = template.Library()

MENU_APP_ORDER = settings.MENU_APP_ORDER
MENU_MODEL_ORDER = settings.MENU_MODEL_ORDER


@register.filter
def sort_apps(apps):
    max_index = len(apps)
    apps.sort(
        key=lambda x:
        MENU_APP_ORDER.index(x['app_label'])
        if x['app_label'] in MENU_APP_ORDER
        else max_index
    )
    return apps


@register.filter
def sort_models(models):
    max_index = len(models)
    models.sort(
        key=lambda x:
        MENU_MODEL_ORDER.index(x['object_name'])
        if x['object_name'] in MENU_MODEL_ORDER
        else max_index
    )
    return models