from django import template

register = template.Library()

"🙄 😊 😒"

@register.filter
def smail(value):
     if value == 0:
         return "🙄"
     elif value > 0:
         return "😊"
     else:
         return "😒"
