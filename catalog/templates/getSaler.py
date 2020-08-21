from django import template
from catalog.models import Saler
register = template.Library()



@register.filter(name='getSaler')
def getSaler(saler):
    return Saler.objects.get(id=saler)
    #return Saler.get_absolute_url(Saler.objects.get(id=saler))
    
@register.filter(name='getAttr')
def getAttr(saler,attr):
    return getattr(saler,attr)
    
@register.filter(name='getUrl')
def getUrl(saler):
    return Saler.get_absolute_url(Saler.objects.get(id=saler))

@register.filter(name='mod')    
def mod(num):
    return num%4