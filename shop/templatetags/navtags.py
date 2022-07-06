from django import template
from ..models import MyDashApp

register = template.Library()

@register.inclusion_tag('shop/all_apps.html')
def mydashapps():
    all_apps = MyDashApp.objects.all()
    return {'all_apps': all_apps}